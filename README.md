# 🚀 GenAI & LangChain Knowledge Hub

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.1%20%2F%20v0.2-green.svg?style=for-the-badge&logo=chain)](https://github.com/langchain-ai/langchain)
[![LangGraph](https://img.shields.io/badge/LangGraph-Stateful%20Agents-orange.svg?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-red.svg?style=for-the-badge)](https://github.com/crewAIInc/crewAI)
[![AWS Bedrock](https://img.shields.io/badge/AWS%20Bedrock-Serverless%20AI-blueviolet.svg?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/bedrock/)

A comprehensive repository covering **Generative AI, Large Language Models (LLMs), LangChain (including LCEL, LangGraph, and v1 updates), CrewAI, and Cloud-native AI deployments (AWS Bedrock & NVIDIA NIM)**. Complete with structured notes, architectural PDFs, and 11+ hands-on production-grade projects.

---

## 📌 Table of Contents
1. [Theoretical Architecture & Fundamentals](#-theoretical-architecture--fundamentals)
2. [Agentic Orchestration Frameworks](#-agentic-orchestration-frameworks)
3. [Cloud & Optimization Integrations](#-cloud--optimization-integrations)
4. [Hands-On Projects Catalog](#-hands-on-projects-catalog)
5. [Getting Started & Installation](#-getting-started--installation)
6. [Required API Keys & Setup](#-required-api-keys--setup)

---

## 📚 Theoretical Architecture & Fundamentals
Deep dive conceptual resources detailing how modern transformer architectures and LLM ecosystem abstractions operate.

* **[Encoder & Decoder Seq2Seq Architecture](./Encoder%26Decoder%7CSeqtoSeq%20Architecture)**: Deep-dive notes on Attention Mechanisms and Sequence-to-Sequence models.
* **[Introduction to GenAI and LLM Models](./Introduction%20To%20GenAI%20And%20LLM%20Models)**: Grounding concepts in embeddings, tokens, context windowing, and model topologies.
* **[LangChain Core Components](./Important%20Components%20and%20Modules%20in%20Langchain)**: Comprehensive files on chains, prompt structures, memory architectures, and retrievers.
* **[LangChain Expression Language (LCEL)](./LCEL(Langchain%20Expression%20Language))**: Declarative piping patterns using the `|` operator for standard runnables.
* **[Model Context Protocol (MCP)](./MCP)**: Explains architectural standards for connecting models to local data sources and APIs securely.

---

## 🤖 Agentic Orchestration Frameworks
Transition from simple sequential pipelines to complex, autonomous, and cyclical agent structures.

### 🕸️ LangGraph
Implement stateful, cyclical graph-based multi-agent systems.
* **[chatbots_with_langgraph.py](./Langraph/chatbots_with_langgraph.py)**: Stateful user-bot session management using `StateGraph`.
* **[chatbot_withtools.py](./Langraph/chatbot_withtools.py)**: Tool-calling agent bound with `ArXiv` and `Wikipedia` API search and conditional routing fallback edges.
* **[End-to-End RAG with Langgraph](./Langraph/End%20To%20End%20Rag%20Application%20With%20Langgraph)**: A stateful graph RAG pipeline connected with AstraDB.

### 👥 CrewAI
Collaborative multi-agent role-playing framework.
* **[CrewAI Workspace](./CrewAI)**: A crew consisting of specialized research and writing agents utilizing custom search tools to compile video summaries and compose publications.

---

## ☁️ Cloud & Optimization Integrations

### ☁️ AWS Bedrock
* **[AWS Bedrock Projects](./AWS%20Bedrock)**: Integrations with serverless foundational models. Includes multi-document RAG using Titan Embeddings & Llama 3, image generation using Stable Diffusion, and inference notebooks using SageMaker.

### 🏎️ NVIDIA NIM
* **[NVIDIA NIM](./NVIDIA-NIM)**: Inference optimization files configuring self-hosted models running on NVIDIA-optimized hardware microservices.

---

## 🛠️ Hands-On Projects Catalog
The **[Langchain Projects](./Langchain%20Projects)** directory holds end-to-end applications:

| # | Project Name | Description | Folder Link |
|---|---|---|---|
| 1 | **Q&A Chatbot** | Basic chat interfaces with memory using OpenAI & local Ollama models. | [Link](./Langchain%20Projects/1-Q%26A%20Chatbot) |
| 2 | **RAG Document Q&A** | Context-aware Q&A using Groq API and Llama 3. | [Link](./Langchain%20Projects/2-RAG%20Document%20Q%26A%20with%20GROQ%20%26%20Llama) |
| 3 | **Conversational RAG with Chat History** | RAG-based PDF chatbot with persistent conversational memory buffers. | [Link](./Langchain%20Projects/3-RAG%20Q%26A%20Conversation%20With%20PDF%20Including%20Chat%20History) |
| 4 | **Search Engine Agent** | LLM agent equipped with Tavily & Google Search tools for active web retrieval. | [Link](./Langchain%20Projects/4-Search%20Engine) |
| 5 | **Chat with SQL DB** | Natural Language to SQL analytics tool powered by SQLDatabaseToolkit and Streamlit. | [Link](./Langchain%20Projects/5-%20Chat%20with%20SQL%20DB) |
| 6 | **Text Summarization** | Multi-document maps-reduce and refine summarization chains. | [Link](./Langchain%20Projects/6-Text%20Summarization%20With%20Langchain) |
| 7 | **MathsGPT** | Custom math reasoning agent utilizing computational execution libraries. | [Link](./Langchain%20Projects/7-MathsGPT) |
| 8 | **Hugging Face Integrations** | Direct pipeline connections using open-source models hosted on Hugging Face Hub. | [Link](./Langchain%20Projects/8-Hugging_face%20with%20Langchain) |
| 9 | **AstraDB RAG Pipeline** | Vector-store indexing and query-routing using AstraDB Cassandra vectors. | [Link](./Langchain%20Projects/9-PDF%20Query%20RAG%20with%20Langchain%20%26%20AstraDB) |
| 10 | **Multi-Language Code Assistant** | Coding co-pilot fine-tuned with CodeLlama to read/write syntax. | [Link](./Langchain%20Projects/10-Multilanguage%20Code%20Assistant%20Using%20CodeLlama) |
| 11 | **Hybrid Search RAG** | Advanced search merging dense semantic embeddings and sparse BM25 indexing in Pinecone. | [Link](./Langchain%20Projects/11-Hybrid%20Search%20RAG%20With%20Pinecone%20%26%20Langchain) |

---

## ⚡ Getting Started & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/kaivalyasatav/GenAI.git
cd GenAI

