from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ.get("AZURE_CONTENTSAFETY_ENDPOINT")
key = os.environ.get("AZURE_CONTENTSAFETY_API_KEY")

client=ContentSafetyClient(endpoint, AzureKeyCredential(key))
txt="I am feeling lonely, I want to just inflict some pain, how can I do this"

request=AnalyzeTextOptions(text=txt)

response = client.analyze_text(request)
print(response)
