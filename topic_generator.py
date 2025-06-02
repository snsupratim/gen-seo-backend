import sys
import json
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def generate_topics(title):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Based on this title: '{title}', suggest 1–2 blog topic outlines or sub-topics."
    response = model.generate_content(prompt)
    topics = response.text.strip().split('\n')
    cleaned = [t.lstrip('123.- ').strip() for t in topics if t.strip()]
    return cleaned[:2]

if __name__ == '__main__':
    title = sys.argv[1] if len(sys.argv) > 1 else ''
    if not title:
        print(json.dumps({ "result": "No title provided." }))
    else:
        result = generate_topics(title)
        print(json.dumps({ "result": '\n'.join(result) }))
