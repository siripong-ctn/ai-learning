from google import genai
from config import GOOGLE_API_KEY

print(GOOGLE_API_KEY)

print("API Key Load Success")
print(f"Key Started: {GOOGLE_API_KEY[:10]}...")

client = genai.Client(api_key=GOOGLE_API_KEY)

models = client.models.list()

print("\nModels Ready:")
for model in models:
    print(model.name)