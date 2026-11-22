from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

question = input("Ask me anything: ")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question
)

print("\nAI Response:")
print(response.text)