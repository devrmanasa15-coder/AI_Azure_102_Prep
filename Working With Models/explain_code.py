import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
import base64


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


# To stream image as binary data and send it
with open("code.py","r", encoding="utf-8") as code_file:  # r read, b binary, reading the image as python object
    code_content=code_file.read()

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps teach how to code",
        },
        {
            "role": "user",
            "content" : f"Explain clearly what the following Python code does: \n\n{code_content}"
            
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat",
    n=2
)
# print("Response 1")
print(response.choices[0].message.content)
