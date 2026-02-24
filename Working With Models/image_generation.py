import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
import base64
import requests

load_dotenv()

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT_2")
model_name = "dall-e-3"
deployment = "dall-e-3"

subscription_key = os.environ.get("AZURE_OPENAI_API_KEY_2")
api_version = "2024-02-01"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.images.generate(
    model = model_name,
    prompt="A futuristic cat dwelling in the sunset, highly detailed, digital art",
    n=1,
    size="1024x1024",
    quality="standard"
)
image_url=response.data[0].url

image_data= requests.get(image_url).content
with open("img2.png","wb") as handler:
    handler.write(image_data)

print("Finished generating the image")