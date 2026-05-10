# AWS Bedrock Generative AI 

A hands-on collection of Generative AI built using Amazon Bedrock and Python (boto3), demonstrating how to interact with multiple foundation models for text generation, conversational AI, and image generation.

## Overview

This folder contains practical implementations of Amazon Bedrock using Python SDK (`boto3`) for experimenting with leading foundation models such as:

- Meta Llama 3
- Anthropic Claude
- Stability AI Stable Diffusion XL
- Amazon Bedrock Converse API
- Bedrock Runtime API

The goal of this project is to provide beginner-friendly and practical examples for developers learning AWS Bedrock and Generative AI application development.

---

## Features

- Text generation using Meta Llama models
- Conversational AI using Anthropic Claude models
- Image generation using Stability AI models
- Amazon Bedrock Converse API examples
- Amazon Bedrock Invoke Model API examples
- JSON payload handling for model invocation
- Base64 image decoding and saving generated outputs
- AWS credential configuration support

---

## Project Structure

```bash
AWS Bedrock/
│
├── llama3.py              # Meta Llama 3 text generation example
├── claude.py             # Anthropic Claude conversational example
├── image_generation.py   # Stable Diffusion image generation
├── requirements.txt      # Python dependencies
├── output/               # Generated images output
└── README.md
