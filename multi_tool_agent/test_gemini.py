import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
print(f"GOOGLE_API_KEY: {os.environ.get('GOOGLE_API_KEY')}")

try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Hello, can you respond with 'Test successful'?")
    print("Response:", response.text)
except Exception as e:
    print(f"Error: {e}")