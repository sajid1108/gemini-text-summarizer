import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables (API key)
load_dotenv()
api_key = os.getenv("GEMINI_API")
genai.configure(api_key=api_key)

# Set up the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Summarization function (same as before)
def summarize(text):
    prompt = f'Summarize the Content with the key points: \n{text}'
    summarized_text = model.generate_content(prompt)
    return summarized_text.text

# Sentiment analysis function
def analyze_sentiment(text):
    prompt = f"Analyze the sentiment of the following text and classify it as Positive, Neutral, or Negative: \n{text}"
    sentiment_result = model.generate_content(prompt)
    sentiment = sentiment_result.text.strip()  # Clean the result
    return sentiment
