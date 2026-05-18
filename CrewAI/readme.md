# 🤖 AI Blog Generator using CrewAI

An intelligent multi-agent AI application built using **CrewAI** that automates **YouTube content research and blog generation** using autonomous AI agents.

This project uses CrewAI agents to search a specific YouTube channel, extract relevant video insights for a given topic, and generate a structured blog post automatically.

---

## 🚀 Project Overview

This project demonstrates the power of **Agentic AI** using CrewAI by creating a collaborative team of AI agents:

- **Blog Researcher Agent** → Searches YouTube videos from a specified channel and gathers relevant information.
- **Blog Writer Agent** → Converts the gathered insights into a well-structured blog post.

The system follows a **sequential multi-agent workflow**, where one agent researches and another writes the final content.

---

## ✨ Features

- Multi-agent orchestration using **CrewAI**
- YouTube channel content analysis
- Automated blog generation from video content
- Sequential task execution
- Agent memory support
- Caching for performance optimization
- Autonomous agent collaboration
- Markdown blog output generation
- OpenAI GPT model integration

---

## 🏗 Architecture

```text
User Input Topic
      │
      ▼
Blog Researcher Agent
(YouTube Channel Search Tool)
      │
      ▼
Extract Relevant Video Insights
      │
      ▼
Blog Writer Agent
(Content Generation using GPT-4)
      │
      ▼
Generated Blog Output (.md file)
```

---

## 🛠 Tech Stack

### Core Technologies
- Python 3.x
- CrewAI
- OpenAI GPT-4
- CrewAI Tools
- python-dotenv

### AI Concepts Used
- Agentic AI
- Multi-Agent Systems
- Autonomous Task Execution
- Prompt Engineering
- LLM-based Content Generation

---

## 📂 Project Structure

```bash
CrewAI/
│
├── crew.py              # Main crew orchestration file
├── agents.py            # AI agent definitions
├── tasks.py             # Task definitions for agents
├── tools.py             # YouTube channel search tool configuration
├── .env                # Environment variables
├── requirements.txt     # Project dependencies
└── new-blog-post.md     # Generated blog output
```

---

## 🤖 Agents Used

### 1. Blog Researcher Agent

**Role:** Blog Researcher from YouTube Videos

Responsibilities:
- Search the specified YouTube channel
- Identify videos relevant to the given topic
- Extract detailed video insights
- Provide structured research data

Capabilities:
- Memory enabled
- Delegation enabled
- Uses YouTube Search Tool

---

### 2. Blog Writer Agent

**Role:** Blog Writer

Responsibilities:
- Analyze research output
- Convert technical content into readable blog format
- Generate compelling blog narratives

Capabilities:
- Memory enabled
- Delegation disabled
- Uses YouTube Search Tool

---

## 📋 Workflow

### Step 1: Research Task
The researcher agent:

- Searches YouTube channel videos
- Identifies topic-specific videos
- Extracts transcription/content insights
- Generates a detailed report

Expected output:
- 3-paragraph comprehensive report

---

### Step 2: Writing Task
The writer agent:

- Uses research findings
- Summarizes extracted information
- Writes a complete blog article
- Saves output as Markdown

Expected output:
- Blog content saved in `new-blog-post.md`
