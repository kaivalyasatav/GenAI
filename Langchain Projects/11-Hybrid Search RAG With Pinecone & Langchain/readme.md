# 🔍 Hybrid Search RAG with Pinecone & LangChain

A production-ready Retrieval-Augmented Generation (RAG) application that combines **semantic vector search** and **keyword-based retrieval (hybrid search)** using **Pinecone**, **LangChain**, and **OpenAI embeddings** for highly accurate question answering.

This project demonstrates how hybrid retrieval improves traditional RAG pipelines by combining dense vector similarity search with sparse lexical matching, leading to better retrieval accuracy for both semantic and exact keyword queries.

---

## 🚀 Project Overview

Traditional RAG systems rely only on semantic vector embeddings, which may miss exact keyword matches.

This project solves that problem using **Hybrid Search Retrieval**, combining:

- **Dense Retrieval** → Semantic similarity search using embeddings
- **Sparse Retrieval** → Keyword/BM25-style lexical matching
- **Pinecone Hybrid Index** → Unified retrieval engine
- **LangChain Orchestration** → Document ingestion, chunking, embedding, and query pipeline

The result is a smarter, more accurate retrieval system for LLM applications.

---

## ✨ Features

- Hybrid search (dense + sparse retrieval)
- Pinecone vector database integration
- LangChain-powered RAG pipeline
- OpenAI embedding model support
- Document chunking & preprocessing
- Better retrieval accuracy than standard vector search
- Fast semantic + keyword document lookup
- Scalable architecture for production AI apps
- Notebook-based experimentation

---

## 🧠 Why Hybrid Search?

Pure vector search struggles with:

❌ Exact technical terms  
❌ Product IDs / codes  
❌ Acronyms  
❌ Rare keywords  
❌ Specific phrase matching

Hybrid search fixes this by combining:

| Retrieval Type | Strength |
|---------------|----------|
| Dense Search | Understands semantic meaning |
| Sparse Search | Matches exact keywords |
| Hybrid Search | Best of both worlds |

Example:

Query:
```text
What is BM25 scoring in information retrieval?
```

Vector search may retrieve semantically related documents.

Hybrid search retrieves:
- semantically relevant content
- exact BM25 keyword matches

Result → higher retrieval precision.

---

## 🏗 System Architecture

```text
Documents
   ↓
Document Loading
   ↓
Text Chunking
   ↓
Embedding Generation
   ↓
Sparse Vector Creation (BM25)
   ↓
Pinecone Hybrid Index Storage
   ↓
User Query
   ↓
Hybrid Retrieval
(Dense + Sparse Matching)
   ↓
Relevant Context Retrieval
   ↓
LLM Response Generation
```

---

## 🛠 Tech Stack

### Core Technologies

- Python
- LangChain
- Pinecone
- OpenAI
- Sentence Transformers
- BM25 / Sparse Retrieval
- Jupyter Notebook

---

## 📁 Project Structure

```bash
11-Hybrid Search RAG With Pinecone & Langchain/
│
├── experiments.ipynb         # Main implementation notebook
├── requirements.txt          # Dependencies
├── .env                      # API keys
├── README.md
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/kaivalyasatav/GenAI.git
cd "GenAI/Langchain Projects/11-Hybrid Search RAG With Pinecone & Langchain"
```

---

### Create Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Dependencies

Main libraries used:

```txt
langchain
pinecone-client
langchain-openai
sentence-transformers
python-dotenv
jupyter
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

## ⚙️ Workflow

### Step 1: Load Documents

The system loads source documents for indexing.

Supported sources can include:
- PDFs
- text documents
- web pages
- structured datasets

---

### Step 2: Split Documents

Documents are chunked into smaller pieces for retrieval efficiency.

Benefits:
- better context granularity
- reduced token waste
- improved retrieval accuracy

---

### Step 3: Generate Dense Embeddings

Semantic embeddings are created using OpenAI embedding models.

Used for:
- meaning-based retrieval
- contextual matching

---

### Step 4: Generate Sparse Representations

Keyword-based sparse vectors are generated using BM25-style retrieval.

Used for:
- exact phrase matching
- rare term retrieval
- acronym search

---

### Step 5: Store in Pinecone

Hybrid vectors are indexed in Pinecone.

Benefits:
- scalable vector search
- low-latency retrieval
- production deployment ready

---

### Step 6: Query Pipeline

User query is processed using hybrid retrieval:

```text
Dense Search + Sparse Search = Hybrid Retrieval
```

Top relevant chunks are returned for LLM generation.

---

## ▶️ Running the Project

Launch Jupyter:

```bash
jupyter notebook
```

Open:

```bash
experiments.ipynb
```

Run notebook cells sequentially.

---

## Example Query

```python
"What is hybrid retrieval in RAG?"
```

Expected behavior:

- semantic understanding of query
- exact keyword matching
- improved retrieval ranking
- better final LLM answers

---

## 📊 Hybrid Search vs Traditional RAG

| Feature | Traditional RAG | Hybrid Search RAG |
|--------|----------------|------------------|
| Semantic understanding | ✅ | ✅ |
| Exact keyword matching | ❌ | ✅ |
| Acronym search | Weak | Strong |
| Rare terminology | Weak | Strong |
| Ranking accuracy | Moderate | High |
| Retrieval robustness | Medium | Excellent |

---

## Real-World Use Cases

This architecture is useful for:

- Enterprise document search
- AI chatbots
- Technical knowledge assistants
- Legal document retrieval
- Medical knowledge search
- Internal company search engines
- Research assistants
- Customer support automation

---

