import sys
import json
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def generate_titles(keyword):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Generate 2 to 3 compelling and SEO-optimized blog titles for the topic: '{keyword}'"
    response = model.generate_content(prompt)
    titles = response.text.strip().split('\n')
    cleaned = [t.lstrip('123.- ').strip() for t in titles if t.strip()]
    return cleaned[:3]

if __name__ == '__main__':
    keyword = sys.argv[1] if len(sys.argv) > 1 else ''
    if not keyword:
        print(json.dumps({ "result": "No keyword provided." }))
    else:
        result = generate_titles(keyword)
        print(json.dumps({ "result": '\n'.join(result) }))
