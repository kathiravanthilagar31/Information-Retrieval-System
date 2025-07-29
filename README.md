# 📚 Information Retrieval System: Document Q&A Chatbot

This repository contains the code for an interactive web application built with Streamlit that allows users to upload multiple PDF documents and then ask questions about their content. Leveraging the capabilities of Large Language Models (LLMs) and vector databases, the app provides conversational answers based on the information retrieved directly from your uploaded files.

---

### ✨ Features:

* **Multi-PDF Upload**: Seamlessly upload one or more PDF documents.
* **Intelligent Q&A**: Ask natural language questions about the content of your uploaded PDFs.
* **Conversational AI**: The chatbot maintains conversation history, allowing for follow-up questions and contextual understanding.
* **Information Retrieval**: Utilizes advanced techniques to retrieve relevant information from documents before generating answers.
* **Clean Interface**: A user-friendly Streamlit interface for easy interaction.

---

### 🛠️ Technologies Used:

* **Streamlit**: For building the interactive web application.
* **Langchain**: For orchestrating the LLM, memory, and retrieval components.
* **OpenAI**: As the Large Language Model (LLM) and Embedding provider (`text-embedding-3-small`).
* **FAISS**: For efficient similarity search and vector storage.
* **PyPDF2**: For extracting text from PDF documents.
* **python-dotenv**: For securely managing API keys.

---

### 🚀 How to Run Locally:

Follow these steps to get your Document Q&A Chatbot up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/kathiravanthilagar31/Information-Retrieval-System.git](https://github.com/kathiravanthilagar31/Information-Retrieval-System.git)
    cd Information-Retrieval-System
    ```

2.  **Create a virtual environment (recommended):**
    It's good practice to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    With your virtual environment activated, install all required packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your OpenAI API Key:**
    Your application requires an OpenAI API key to interact with the LLM and embedding models.
    * Create a new file named `.env` in the **root directory** of your project (the same directory as `app.py` and `requirements.txt`).
    * Add your OpenAI API key to this file in the following format:
        ```
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
        (Replace `"your_openai_api_key_here"` with your actual OpenAI API key.)

5.  **Run the Streamlit application:**
    From the root directory of your project (where `app.py` is located), execute the following command:
    ```bash
    streamlit run app.py
    ```
    This command will start the Streamlit server, and your app will automatically open in your default web browser.

---
