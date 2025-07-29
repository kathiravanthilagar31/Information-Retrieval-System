import streamlit as st
from src.helper import get_text_from_pdf,get_chunks,get_vectorstore,get_conversation_chain
from langchain_core.messages import AIMessage,HumanMessage

def user_input():
    response=st.session_state.conversation({'question':st.session_state.user_question_input})
    st.session_state.chatHistory=response['chat_history']
    st.session_state.user_question_input = ""
    

def chat_history(chat_placeholder):
    chat_placeholder.empty()
    if st.session_state.chatHistory:
        with chat_placeholder.container():
            for message in st.session_state.chatHistory:
                if isinstance(message, HumanMessage):
                    st.write("User:",message.content)
                else:
                    st.write("AI:",message.content)

        
def main():
    st.set_page_config("Information Retrieval")
    st.title("Information Retrieval System")

    if "user_question_input" not in st.session_state:
        st.session_state.user_question_input = ""
    if "conversation" not in st.session_state:
        st.session_state.conversation=None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory=[]
    if "show_success_message" not in st.session_state:
        st.session_state.show_success_message = False

    chat_messages_placeholder = st.empty()
        
    st.text_input("Ask anything about your PDF files..",
                                key="user_question_input",
                                value=st.session_state.user_question_input,
                                on_change=user_input)

    chat_history(chat_messages_placeholder) 
        
    with st.sidebar:
        st.title("File Uploader")
        pdf_docs=st.file_uploader("Upload you PDF files here.",accept_multiple_files=True)
        
        try:
            if st.button("Submit and Initiate Chat"):
                if not pdf_docs:
                    st.error('Please upload atleast one PDF file to proceed.')
                else:
                    with st.spinner("processing"):
                        raw_text=get_text_from_pdf(pdf_docs)
                        text_chunk=get_chunks(raw_text)
                        if not text_chunk:
                            st.error("No text could be extracted or chunks created from the uploaded PDF(s). Please ensure the PDFs contain selectable text.")
                            st.session_state.conversation = None
                            st.session_state.chatHistory = []
                            return
                        vectordb=get_vectorstore(text_chunk)
                        st.session_state.conversation=get_conversation_chain(vectordb)
                        st.session_state.chatHistory=[]
                        st.session_state.chatHistory.append(AIMessage(content="Welcome!"))
                        st.session_state.show_success_message = True
                        chat_messages_placeholder.empty()
                        chat_history(chat_messages_placeholder)
                        st.rerun()
        except Exception as e:
            st.error(f'An error occurred during processing: {e}. Please check your .pdf file or try again with a different file')
            
    if st.session_state.show_success_message:
        st.success('Done!')
        st.session_state.show_success_message = False
    

if __name__=="__main__":
    main()
