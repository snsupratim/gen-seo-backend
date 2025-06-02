import sys
import json
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def generate_content(topic):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Write a 150-word SEO-optimized article about: {topic}"
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == '__main__':
    topic = sys.argv[1]
    content = generate_content(topic)
    print(json.dumps({"content": content}))
