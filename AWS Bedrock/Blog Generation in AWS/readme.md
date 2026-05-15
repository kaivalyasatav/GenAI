# AI Blog Generation using AWS Bedrock

An AI-powered serverless blog generation application built using **Amazon Bedrock, Meta Llama 3, AWS Lambda, AWS API Gateway, Amazon S3, and Boto3**.

This project exposes a REST API endpoint through AWS API Gateway that accepts blog topic requests, triggers an AWS Lambda function, generates AI-written blog content using Meta Llama 3 via Amazon Bedrock, and automatically stores the generated output in Amazon S3.

The application demonstrates a complete cloud-native event-driven generative AI workflow.
---

## Features

- AI-powered blog generation
- Amazon Bedrock integration
- Meta Llama 3 inference
- AWS Lambda serverless execution
- AWS API Gateway REST API integration
- Route and stage deployment configuration
- Amazon S3 blog storage
- Prompt-driven content generation
- Automatic timestamp-based file creation
- Retry handling for Bedrock API calls
- Cloud-native event-driven architecture
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
Client Request
     │
     ▼
AWS API Gateway
(Route + Stage)
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
Meta Llama 3 Foundation Model
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

## API Gateway Configuration

AWS API Gateway was used to expose the Lambda function as a REST API endpoint.

### Configuration Steps

1. Create an API in AWS API Gateway
2. Create a route (e.g. `/generate-blog`)
3. Integrate the route with the AWS Lambda function
4. Configure request payload handling
5. Create deployment stage (e.g. `dev` / `prod`)
6. Deploy the API

Example endpoint:

```bash
https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/generate-blog
```

Sample POST request:

```json
{
  "blog_topic": "Future of Artificial Intelligence"
}
```

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

## How It Works

1. Client sends a POST request to the API Gateway endpoint
2. API Gateway route forwards the request to AWS Lambda
3. Lambda extracts the blog topic from the event payload
4. A prompt is dynamically generated for Meta Llama 3
5. Amazon Bedrock processes the request and generates blog content
6. Lambda extracts the generated response
7. Blog content is stored in Amazon S3 using timestamp-based filenames
8. API returns success response to the client

## Learning Concepts Covered

This project demonstrates:

- Amazon Bedrock integration
- Meta Llama 3 inference
- AWS Lambda serverless execution
- AWS API Gateway REST API deployment
- Route and stage configuration
- Amazon S3 storage automation
- Event-driven cloud architecture
- Prompt engineering
- Boto3 integrations
- Generative AI cloud workflows

