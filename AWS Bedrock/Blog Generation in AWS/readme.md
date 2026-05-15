# AI Blog Generation using AWS Bedrock

An AI-powered serverless blog generation application built using **Amazon Bedrock, Meta Llama 3, AWS Lambda, Amazon S3, and Boto3**.

This project generates AI-written blog content based on a user-provided topic using Meta Llama 3 through Amazon Bedrock, then automatically stores the generated blog output in an Amazon S3 bucket for persistence.

---

## Features

- AI-powered blog generation
- Amazon Bedrock integration
- Meta Llama 3 inference
- AWS Lambda serverless execution
- Amazon S3 blog storage
- Prompt-driven content generation
- Automatic timestamp-based file creation
- Error handling with retry configuration
- Cloud-native architecture

---

## Tech Stack

### Cloud Services
- AWS Lambda
- Amazon Bedrock
- Amazon S3

### AI / LLM
- Meta Llama 3 (8B Instruct)
- Foundation Models
- Prompt Engineering

### Backend
- Python
- Boto3
- Botocore

---

## Project Architecture

```text
User Request / API Event
          │
          ▼
AWS Lambda Function
          │
          ▼
Prompt Construction
          │
          ▼
Amazon Bedrock Runtime API
          │
          ▼
Meta Llama 3 Model
          │
          ▼
Generated Blog Content
          │
          ▼
Amazon S3 Storage
```

---

## Project Structure

```bash
Blog Generation in AWS/
│
├── lambda_function.py      # Main Lambda function
├── README.md              # Documentation
└── requirements.txt       # Dependencies (optional)
```

---

## How It Works

1. User sends a request containing a blog topic
2. AWS Lambda receives the event payload
3. A prompt is dynamically created for the Llama 3 model
4. Amazon Bedrock generates blog content
5. Generated output is extracted from the response
6. Blog content is saved to Amazon S3 with timestamp-based filenames
7. Lambda returns success response

---

## Sample Input

```json
{
  "body": "{\"blog_topic\":\"Future of Artificial Intelligence\"}"
}
```

---

## Sample Output

Generated blog file stored in:

```bash
s3://awsbedrockgenaiks/blog-output/153045.txt
```

Lambda response:

```json
{
  "statusCode": 200,
  "body": "Blog Generation is completed"
}
```

---

## AWS Setup

### 1. Configure AWS Credentials

```bash
aws configure
```

Provide:

```bash
AWS Access Key ID
AWS Secret Access Key
Region: us-east-1
```

---

### 2. Enable Bedrock Model Access

Go to:

AWS Console → Amazon Bedrock → Model Access

Enable:

- Meta Llama 3 8B Instruct

---

### 3. Create S3 Bucket

Create a bucket:

```bash
awsbedrockgenaiks
```

Or update the code with your own bucket name:

```python
s3_bucket='your-bucket-name'
```

---

### 4. Create Lambda Function

Deploy the Python code to AWS Lambda.

Set:

- Runtime: Python 3.x
- Timeout: 5+ minutes
- Memory: 512 MB or higher

---

### 5. IAM Permissions

Attach permissions for:

- Bedrock model invocation
- S3 object write access

Required actions:

```json
bedrock:InvokeModel
s3:PutObject
```

---

## Example Prompt

The Lambda dynamically generates prompts like:

```text
Write a 200-word blog on Artificial Intelligence
```

---

## Learning Concepts Covered

This project demonstrates:

- Amazon Bedrock integration
- Meta Llama 3 inference
- Serverless AI application design
- AWS Lambda event-driven execution
- S3 object storage automation
- Prompt engineering
- Cloud-native generative AI workflows
- Boto3 API integrations
- Error handling and retries

