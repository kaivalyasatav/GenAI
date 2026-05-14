# Chat with SQL Database using LangChain

An AI-powered Natural Language SQL Assistant that enables users to interact with relational databases using plain English queries.

This project leverages **LangChain, OpenAI LLMs, SQLAlchemy, and Streamlit** to convert natural language questions into SQL queries, execute them securely, and return meaningful database insights through a conversational interface. LangChain’s SQL database toolkit is designed specifically for LLM-driven interaction with SQL databases. :contentReference[oaicite:0]{index=0}

---

## Features

- Natural language to SQL query conversion
- Conversational database interaction
- SQL query execution and response generation
- Support for relational databases
- Schema-aware query generation
- Interactive Streamlit UI
- LLM-powered analytics assistant
- Real-time query handling
- Error handling for invalid queries
- Business intelligence style question answering

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain
- SQLAlchemy

### AI / LLM
- OpenAI GPT Models
- LangChain SQL Agent

### Database
- MySQL / SQLite / PostgreSQL (depending on configuration)

---

## Project Architecture

```text
User Query (Natural Language)
           │
           ▼
Streamlit Chat Interface
           │
           ▼
LangChain SQL Agent
           │
           ▼
Schema Inspection
           │
           ▼
SQL Query Generation
           │
           ▼
Database Execution
           │
           ▼
Query Results
           │
           ▼
AI-generated Response
```

---

## Project Structure

```bash
5- Chat with SQL DB/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
├── database/               # Database files / configs
│   └── sample.db
└── utils.py                # Helper functions (if applicable)
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kaivalyasatav/GenAI.git
cd "GenAI/Langchain Projects/5- Chat with SQL DB"
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

If no requirements file exists:

```bash
pip install streamlit langchain openai sqlalchemy pymysql
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Or export directly:

Mac/Linux:

```bash
export OPENAI_API_KEY=your_key
```

Windows:

```bash
set OPENAI_API_KEY=your_key
```

---

## Database Configuration

Update your database connection string inside the project:

### SQLite Example

```python
sqlite:///sample.db
```

### MySQL Example

```python
mysql+pymysql://username:password@localhost/database_name
```

### PostgreSQL Example

```python
postgresql://username:password@localhost/database_name
```

---

## Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

## Example Queries

Ask questions like:

```bash
Show all customers from Pune
```

```bash
What is the total revenue this month?
```

```bash
List top 5 products by sales
```

```bash
How many orders were placed last week?
```

```bash
Which customers generated the highest revenue?
```

---

## How It Works

1. User enters a natural language query
2. LangChain inspects database schema
3. LLM understands the request
4. SQL query is generated automatically
5. Query executes on connected database
6. Results are formatted into human-readable response

---

## Use Cases

- Business intelligence assistant
- SQL analytics chatbot
- Data exploration assistant
- Database Q&A system
- Enterprise analytics automation
- Reporting assistant
- Internal data assistant

---

## Learning Concepts Covered

This project demonstrates:

- LangChain SQL Agents
- Natural Language Processing
- Text-to-SQL conversion
- LLM orchestration
- Database schema understanding
- SQL query generation
- Streamlit deployment
- Conversational analytics
- AI-powered database interaction

---

## Security Note

Because LLM-generated SQL executes against a database, database permissions should be tightly scoped (prefer read-only access where possible). LangChain also highlights this risk in its SQL toolkit guidance. :contentReference[oaicite:1]{index=1}

---
