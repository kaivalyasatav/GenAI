import boto3
import json


prompt_data = "Act as Shakespeare and write a poem on Generative AI"

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

response = bedrock.converse(
    modelId="arn:aws:bedrock:us-east-1:566208417193:inference-profile/us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {"text": prompt_data}
            ]
        }
    ],
    inferenceConfig={
        "maxTokens": 2000,
        "temperature": 1,
    }
)

print(response["output"]["message"]["content"][0]["text"])