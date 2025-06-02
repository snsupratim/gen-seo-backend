import sys
import json
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def generate_keywords(seed_keyword):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Suggest 3 to 5 SEO-friendly keywords related to: '{seed_keyword}'"
    response = model.generate_content(prompt)
    keywords = response.text.strip().split('\n')
    cleaned = [k.lstrip('12345.- ').strip() for k in keywords if k.strip()]
    return cleaned[:5]

if __name__ == '__main__':
    keyword = sys.argv[1] if len(sys.argv) > 1 else ''
    if not keyword:
        print(json.dumps({ "result": "No keyword provided." }))
    else:
        result = generate_keywords(keyword)
        print(json.dumps({ "result": '\n'.join(result) }))
