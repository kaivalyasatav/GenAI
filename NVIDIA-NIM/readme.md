# NVIDIA NIM RAG PDF Chatbot

An intelligent Retrieval-Augmented Generation (RAG) chatbot built using NVIDIA NIM, LangChain, FAISS, and Streamlit that allows users to ask questions from PDF documents and receive accurate context-based responses.

## Project Overview

This project demonstrates how to build a document-aware AI assistant using Retrieval-Augmented Generation (RAG). The application loads PDF documents, converts them into vector embeddings using NVIDIA Embeddings, stores them in a FAISS vector database, and retrieves the most relevant chunks to generate precise answers using NVIDIA’s LLM.

The chatbot answers user queries strictly based on the uploaded document context, making it useful for document analysis, knowledge extraction, research assistance, and enterprise Q&A systems.

---

## Features

- PDF document ingestion
- Automatic document chunking
- Vector embeddings using NVIDIA AI Endpoints
- Fast similarity search using FAISS
- Retrieval-Augmented Generation (RAG)
- Context-aware question answering
- Interactive Streamlit user interface
- Document similarity search viewer
- Efficient retrieval pipeline using LangChain

---

## Tech Stack

### Frontend
- Streamlit

### Backend / AI Framework
- Python
- LangChain

### LLM & Embeddings
- NVIDIA NIM
- Meta Llama 3.1 70B Instruct
- NVIDIA Embeddings

### Vector Database
- FAISS

### Document Processing
- PyPDFDirectoryLoader
- RecursiveCharacterTextSplitter

---

## Architecture

```text
PDF Documents
     ↓
Document Loader (PyPDFDirectoryLoader)
     ↓
Text Chunking (RecursiveCharacterTextSplitter)
     ↓
Embedding Generation (NVIDIA Embeddings)
     ↓
FAISS Vector Store
     ↓
Similarity Retrieval
     ↓
Meta Llama 3.1 70B (NVIDIA NIM)
     ↓
Final Answer Generation
     ↓
Streamlit UI
```

---

## Project Workflow

### 1. Document Loading
The application loads PDF documents from the `us_census` directory using:

```python
PyPDFDirectoryLoader("./us_census")
```

---

### 2. Text Chunking
Documents are split into smaller chunks for efficient retrieval:

```python
RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=50
)
```

This improves semantic search performance and preserves context continuity.

---

### 3. Embedding Generation
Each text chunk is converted into vector embeddings using NVIDIA’s embedding model:

```python
NVIDIAEmbeddings()
```

---

### 4. Vector Storage
Embeddings are stored in FAISS for efficient nearest-neighbor similarity search:

```python
FAISS.from_documents()
```

---

### 5. Retrieval-Augmented Generation
When a user asks a question:

- Relevant chunks are retrieved from FAISS
- Retrieved context is passed to the LLM
- The LLM generates an answer strictly based on document context

---

## Folder Structure

```text
NVIDIA-NIM-RAG/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── us_census/
    ├── file1.pdf
    ├── file2.pdf
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/nvidia-nim-rag-chatbot.git
cd nvidia-nim-rag-chatbot
```

---

### Create Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a `requirements.txt` file:

```txt
streamlit
langchain
langchain-community
langchain-core
langchain-classic
langchain-text-splitters
langchain-nvidia-ai-endpoints
faiss-cpu
pypdf
python-dotenv
```

---

## Environment Variables

Create a `.env` file:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

Get your API key from NVIDIA AI Endpoints.

---

## Run the Application

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## Usage

### Step 1
Place your PDF files inside:

```text
us_census/
```

### Step 2
Run the Streamlit app.

### Step 3
Click:

```text
Documents Embedding
```

This will:

- Load PDFs
- Split documents
- Generate embeddings
- Create FAISS vector database

### Step 4
Ask questions such as:

```text
What is the population growth mentioned in the report?
```

```text
Summarize the key findings from the document.
```

```text
What demographic insights are available?
```

---
