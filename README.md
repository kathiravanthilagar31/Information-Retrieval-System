# 📚 Information Retrieval System: Document Q&A Chatbot

This repository contains the code for an interactive web application built with Streamlit that allows users to upload multiple PDF documents and then ask questions about their content. Leveraging the capabilities of Large Language Models (LLMs) and vector databases, the app provides conversational answers based on the information retrieved directly from your uploaded files.

---

### ✨ Features:

* **Multi-PDF Upload**: Seamlessly upload one or more PDF documents.
* **Intelligent Q&A**: Ask natural language questions about the content of your uploaded PDFs.
* **Comprehensive Document Processing**: Extracts text from regular digital content, structured tables, and even text within images (via OCR).
* **Conversational AI**: The chatbot maintains conversation history, allowing for follow-up questions and contextual understanding.
* **Information Retrieval**: Utilizes advanced techniques to retrieve relevant information from documents before generating answers.
* **Clean Interface**: A user-friendly Streamlit interface for easy interaction.

---

### 🛠️ Technologies Used:

* **Streamlit**: For building the interactive web application.
* **Langchain**: For orchestrating the LLM, memory, and retrieval components.
* **langchain-openai**: Langchain's integration for OpenAI models.
* **langchain-community**: Community integrations for Langchain, including FAISS.
* **OpenAI**: As the Large Language Model (LLM) and Embedding provider (`text-embedding-3-small`).
* **FAISS**: For efficient similarity search and vector storage.
* **PyMuPDF (`pymupdf`)**: For robust PDF parsing, including extraction of digital text, structured tables, and text from images (OCR).
* **pandas**: Used for processing and converting extracted table data.
* **python-dotenv**: For securely managing API keys.
* **Tesseract-OCR**: An external OCR engine (installed via `packages.txt`) used by PyMuPDF for image-based text extraction.

---

### 🚀 How to Run Locally:

Follow these steps to get your Document Q&A Chatbot up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kathiravanthilagar31/Information-Retrieval-System.git
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

3.  **Install Python dependencies:**
    With your virtual environment activated, install all required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Install External System Dependencies (Tesseract-OCR):**
    For OCR capabilities, you need to install Tesseract-OCR on your system.
    * **On Debian/Ubuntu (e.g., Streamlit Community Cloud):**
        Create a file named `packages.txt` in your repository's root with the following content:
        ```
        tesseract-ocr
        ```
    * **On Windows (local development):**
        Download and install Tesseract from [https://tesseract-ocr.github.io/tessdoc/Installation.html](https://tesseract-ocr.github.io/tessdoc/Installation.html). Make sure to add it to your system's PATH.
    * **On macOS (local development):**
        ```bash
        brew install tesseract
        ```

5.  **Set up your OpenAI API Key:**
    Your application requires an OpenAI API key to interact with the LLM and embedding models.
    * Create a new file named `.env` in the **root directory** of your project (the same directory as `app.py` and `requirements.txt`).
    * Add your OpenAI API key to this file in the following format:
        ```
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
        (Replace `"your_openai_api_key_here"` with your actual OpenAI API key.)

6.  **Run the Streamlit application:**
    From the root directory of your project (where `app.py` is located), execute the following command:
    ```bash
    streamlit run app.py
    ```
    This command will start the Streamlit server, and your app will automatically open in your default web browser.

---
