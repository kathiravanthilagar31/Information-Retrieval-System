import streamlit as st
from src.helper import get_text_from_pdf,get_chunks,get_vectorstore,get_conversation_chain


def user_input():
    response=st.session_state.conversation({'question':st.session_state.user_question_input})
    st.session_state.chatHistory=response['chat_history']
    st.session_state.user_question_input = ""
    

def chat_history():
    if st.session_state.chatHistory:
        for i,message in enumerate(st.session_state.chatHistory):
            if i%2==0:
                st.write("User:",message.content)
            else:    
                st.write("Reply:",message.content)

        
def main():
    st.set_page_config("Information Retrieval")
    st.title("Information Retrieval System")

        
    user_question=st.text_input("Ask anything about your PDF files..",
                                key="user_question_input",
                                value=st.session_state.user_question_input,
                                on_change=user_input)

    if "conversation" not in st.session_state:
        st.session_state.conversation=None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory=None

    chat_history() 
        
    with st.sidebar:
        st.title("File Uploader")
        pdf_docs=st.file_uploader("Upload you PDF files here.",accept_multiple_files=True)
    
        if st.button("Submit and Initiate Chat"):
            with st.spinner("processing"):
                raw_text=get_text_from_pdf(pdf_docs)
                text_chunk=get_chunks(raw_text)
                vectordb=get_vectorstore(text_chunk)
                st.session_state.conversation=get_conversation_chain(vectordb)
                st.success('Done')
                
if __name__=="__main__":
    main()