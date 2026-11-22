import os
from dotenv import load_dotenv

load_dotenv()

def get_google_api_key():
  load_dotenv()
  api_key = os.getenv("GOOGLE_API_KEY")
  if not api_key:
    raise ValueError("GOOGLE_API_KEY Not found")
  return api_key

GOOGLE_API_KEY = get_google_api_key()