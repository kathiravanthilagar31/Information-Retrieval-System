📚 Document Q&A Chatbot with Streamlit & Langchain
This is the repository for the Information Retrieval System, a powerful and interactive web application built with Streamlit. It allows users to upload multiple PDF documents and then ask questions about their content. Leveraging the capabilities of Large Language Models (LLMs) and vector databases, the app provides conversational answers based on the information retrieved directly from your uploaded files.

✨ Features:
Multi-PDF Upload: Seamlessly upload one or more PDF documents.

Intelligent Q&A: Ask natural language questions about the content of your uploaded PDFs.

Conversational AI: The chatbot maintains conversation history, allowing for follow-up questions and contextual understanding.

Information Retrieval: Utilizes advanced techniques to retrieve relevant information from documents before generating answers.

Clean Interface: A user-friendly Streamlit interface for easy interaction.

🛠️ Technologies Used:
Streamlit: For building the interactive web application.

Langchain: For orchestrating the LLM, memory, and retrieval components.

OpenAI: As the Large Language Model (LLM) and Embedding provider (text-embedding-3-small).

FAISS: For efficient similarity search and vector storage.

PyPDF2: For extracting text from PDF documents.

python-dotenv: For securely managing API keys.

🚀 How to Run Locally:
Clone the repository:

Bash

git clone https://github.com/kathiravanthilagar31/Information-Retrieval-System.git
cd Information-Retrieval-System
(Remember to replace your-username with your actual GitHub username if you're providing this for others to clone.)

Create a virtual environment (recommended):

Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Set up your OpenAI API Key:

Create a file named .env in the root directory of your project (same level as app.py).

Add your OpenAI API key to this file:

OPENAI_API_KEY="your_openai_api_key_here"
(Replace your_openai_api_key_here with your actual key.)

Run the Streamlit application:

Bash

streamlit run app.py
Your app will open in your default web browser!

