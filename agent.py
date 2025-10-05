# agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def run_agent(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return " Gemini API Key not found."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f" Error generating itinerary: {e}"
