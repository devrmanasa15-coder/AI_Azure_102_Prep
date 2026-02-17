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
with open("azure-vm-diagram.png","rb") as image_file:  # r read, b binary, reading the image as python object
    image_details=base64.b64encode(image_file.read()).decode("utf-8")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant who helps to describe images",
        },
        {
            "role": "user",
            "content" :
            [
                {
                    "type":"text",
                    "text":"Give me a description of what the image is trying to explain"
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/png;base64,{image_details}"
                    }
                }
            ]
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