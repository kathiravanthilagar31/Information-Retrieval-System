import os
import fitz
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from dotenv import load_dotenv




load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

def get_text_from_pdf(pdf_docs):
    full_extracted_text = ""
    for pdf_file_obj in pdf_docs:
            # PyMuPDF can open directly from bytes (Streamlit UploadedFile's .read() provides bytes)
            doc = fitz.open(stream=pdf_file_obj.read(), filetype="pdf")
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                page_content = []

                # 1. Extract regular digital text
                digital_text = page.get_text("text")
                if digital_text.strip():
                    page_content.append(digital_text)

                # 2. Extract structured tables
                tables = page.find_tables()
                if tables.tables: # .tables is the list of found table objects
                    for table in tables.tables:
                        try:
                            table_data = table.extract()
                            if table_data:
                                # Convert table data to a Pandas DataFrame and then to Markdown for RAG
                                # Assuming first row is header, rest is data
                                if table_data[0]: # Check if header exists
                                    df = pd.DataFrame(table_data[1:], columns=table_data[0])
                                else: # No header, just data
                                    df = pd.DataFrame(table_data)
                                
                                page_content.append("--- TABLE START ---\n" + df.to_markdown(index=False) + "\n--- TABLE END ---")
                        except Exception as table_e:
                            print(f"Warning: Error extracting structured table on page {page_num} of '{pdf_file_obj.name}': {table_e}")
                            # Fallback: if structured extraction fails, try to get unstructured text from table area
                            # This might already be covered by digital_text, but as a fallback
                            table_bbox = table.bbox # Get bounding box of the table
                            unstructured_table_text = page.get_text(clip=table_bbox)
                            if unstructured_table_text.strip():
                                page_content.append("--- TABLE (UNSTRUCTURED) ---\n" + unstructured_table_text + "\n--- TABLE END ---")


                # 3. Perform OCR for text in images (only if digital text is very sparse or missing)
                # This is a heuristic to avoid unnecessary OCR on text-rich pages.
                # Check if the page has significant image content but little digital text.
                # page.get_pixmap().size gives total pixels, a rough indicator of image presence.
                if len(digital_text.strip()) < 100 and page.get_pixmap().size > 50000: # Adjust thresholds as needed
                    try:
                        # get_textpage_ocr() returns a TextPage object
                        # flags=0 for plain text. Requires Tesseract-OCR installed on the system.
                        ocr_text_page = page.get_textpage_ocr(flags=0)
                        ocr_text = ocr_text_page.extractText()
                        if ocr_text.strip(): # Only add if OCR actually found text
                            page_content.append("--- OCR TEXT START ---\n" + ocr_text + "\n--- OCR TEXT END ---")
                    except Exception as ocr_e:
                        print(f"Warning: OCR failed on page {page_num} of '{pdf_file_obj.name}': {ocr_e}. Tesseract might not be installed or TESSDATA_PREFIX is incorrect.")
                        # This error means Tesseract couldn't run, not necessarily that there's no text.

                # Combine all extracted content for the current page
                if page_content:
                    full_extracted_text += "\n\n--- PAGE BREAK (Page " + str(page_num + 1) + ") ---\n\n"
                    full_extracted_text += "\n\n".join(page_content)
            
            doc.close()
    return full_extracted_text

def get_chunks(full_extracted_text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
    chunks=text_splitter.split_text(full_extracted_text)
    return chunks

def get_vectorstore(chunks):
    Embedding=OpenAIEmbeddings(model="text-embedding-3-small")
    vectordb=FAISS.from_texts(chunks,embedding=Embedding)
    return vectordb

def get_conversation_chain(vectordb):
    llm=OpenAI()
    memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain=ConversationalRetrievalChain.from_llm(llm=llm,retriever=vectordb.as_retriever(),memory=memory)
    return conversation_chain