import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize(text):
    prompt = f'Summarize the Content with the key points: \n{text}'
    summarized_text = model.generate_content(prompt)
    return summarized_text.text
