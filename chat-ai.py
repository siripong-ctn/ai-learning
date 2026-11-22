from google import genai
from config import GOOGLE_API_KEY
import time

client = genai.Client(api_key=GOOGLE_API_KEY)

question = input("Ask me anything: ")

print("\nThinking...", end="", flush=True)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )

    print("\r" + " " * 20 + "\r", end="")

    print("AI Response:\n")
    print(response.text)

except Exception:
    print("\r" + " " * 20 + "\r", end="")

    print("AI service is currently busy.")