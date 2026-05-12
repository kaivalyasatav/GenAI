# Chat PDF with AWS Bedrock & Llama 3

An intelligent PDF Question Answering chatbot built using **Amazon Bedrock, Meta Llama 3, LangChain, FAISS, and Streamlit**.

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to upload PDF documents, generate embeddings, store them in a vector database, and ask context-aware questions from the documents. Amazon Bedrock provides managed access to models like Meta Llama through a unified API. :contentReference[oaicite:0]{index=0}

---

## Features

- Chat with PDF documents
- Retrieval-Augmented Generation (RAG)
- Amazon Bedrock integration
- Meta Llama 3 inference
- Amazon Titan embeddings
- FAISS vector database
- Semantic similarity search
- PDF document ingestion
- Streamlit interactive UI
- Error handling and validation
- Local vector store persistence

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain
- Boto3
- AWS Bedrock

### AI / ML
- Meta Llama 3
- Amazon Titan Embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database
- FAISS

### Document Processing
- PyPDF
- RecursiveCharacterTextSplitter

---

## Project Architecture

```text
PDF Documents
     │
     ▼
PDF Loader (PyPDF)
     │
     ▼
Text Chunking
(RecursiveCharacterTextSplitter)
     │
     ▼
Amazon Titan Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Similarity Search Retrieval
     │
     ▼
Meta Llama 3 (AWS Bedrock)
     │
     ▼
Final AI Response
```

---

## Project Structure

```bash
Chat PDF With AWS Bedrock With LLama3/
│
├── app.py                  # Main Streamlit chatbot application
├── requirements.txt        # Python dependencies
├── README.md              # Documentation
├── data/                  # Input PDF files
│   ├── sample1.pdf
│   ├── sample2.pdf
│   └── ...
│
└── faiss_index/           # Generated vector database
    ├── index.faiss
    └── index.pkl
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kaivalyasatav/GenAI.git
cd "GenAI/AWS Bedrock/Chat PDF With AWS Bedrock With LLama3"
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

If you don't have a requirements file:

```bash
pip install streamlit boto3 langchain langchain-aws langchain-community langchain-core langchain-text-splitters faiss-cpu pypdf
```

---

## AWS Setup

Configure AWS credentials:

```bash
aws configure
```

Provide:

```bash
AWS Access Key ID
AWS Secret Access Key
Region: us-east-1
Output format: json
```

---

## Enable Bedrock Models

Go to:

AWS Console → Amazon Bedrock → Model Access

Enable:

- Amazon Titan Embeddings
- Meta Llama 3 8B Instruct

---

## How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

## How to Use

### Step 1: Add PDFs

Place your PDF files inside:

```bash
data/
```

Example:

```bash
data/
 ├── machine_learning_notes.pdf
 ├── research_paper.pdf
```

---

### Step 2: Create Vector Store

Click:

```bash
Create / Update Vectors
```

This will:

- Load PDF documents
- Split text into chunks
- Generate embeddings
- Store vectors in FAISS

---

### Step 3: Ask Questions

Example:

```bash
What is machine learning?
```

```bash
Summarize chapter 2.
```

```bash
Explain the key findings of this paper.
```

---

### Step 4: Get Response

Click:

```bash
Get Answer
```

The chatbot retrieves relevant chunks and generates an answer using Meta Llama 3.

---

## Example Use Cases

- Research paper Q&A
- Resume/document analysis
- Academic assistant
- Internal knowledge chatbot
- PDF summarization
- Legal/technical document querying
- Enterprise document search

---

## Learning Concepts Covered

This project demonstrates:

- Amazon Bedrock
- Foundation Models
- Meta Llama 3 Integration
- Vector Databases
- Embeddings
- FAISS
- Semantic Search
- RAG Architecture
- LangChain
- Streamlit Deployment


