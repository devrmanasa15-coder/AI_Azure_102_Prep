'''Getting some input from user either in form of images or text, 
first we filter that using content safety filter before passing it on the LLM'''

from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ.get("AZURE_CONTENTSAFETY_ENDPOINT")
key = os.environ.get("AZURE_CONTENTSAFETY_API_KEY")

client = ContentSafetyClient(endpoint, AzureKeyCredential(key))
with open("img1.jpg", "rb") as image_file:
    request = AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response = client.analyze_image(request)
print(response)
