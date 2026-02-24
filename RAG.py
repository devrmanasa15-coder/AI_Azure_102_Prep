import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import base64


load_dotenv()

endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
model_name = "gpt-4.1"
deployment = "gpt-4.1"

subscription_key = os.environ.get("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)
rag_params = {
    "data_sources":[
        {
            "type":"azure_search",
            "parameters":{
                "endpoint":os.environ.get("AZURE_SEARCH_ENDPOINT"),
                "index_name":"dataindex",
                "authentication":{
                    "type":"api_key",
                    "key": os.environ.get("AZURE_SEARCH_API_KEY")
                }
            }
        }
    ]
}
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is attention mechanism architecture"

        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-4.1",
    n=2,
    extra_body=rag_params
)

print(response.choices[0].message.content)
