import boto3
import json
prompt_data = "Act as Shakespeare and write a poem on Generative AI"

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

response = bedrock.converse(
    modelId="meta.llama3-8b-instruct-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {"text": prompt_data}
            ]
        }
    ],
    inferenceConfig={
        "maxTokens": 512,
        "temperature": 0.5,
        "topP": 0.9
    }
)

print(response["output"]["message"]["content"][0]["text"])