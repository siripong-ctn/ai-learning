import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY Not found")

print("API Key Load Success")
print(f"Key Started: {api_key[:10]}...")

client = genai.Client(api_key=api_key)

models = client.models.list()

print("\nModels Ready:")
for model in models:
    print(model.name)