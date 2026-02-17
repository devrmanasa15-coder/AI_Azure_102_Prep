import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv


load_dotenv()

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key = os.environ.get("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant helping students to learn about Large Language Models",
        },
        {
            "role": "user",
            "content": "What is temperature setting",
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat",
    n=2
)
# print("Response 1")
# print(response.choices[0].message.content)
# print("Response 2")
# print(response.choices[0].message.content)

# Formatting the response
dumped_response = response.model_dump(mode="json") 
print(json.dumps(dumped_response, indent=2))