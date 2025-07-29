import os
from PyPDF2 import PdfReader
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
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
    chunks=text_splitter.split_text(text)
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