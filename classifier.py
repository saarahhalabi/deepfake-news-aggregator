import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def classify_article(title, content):
    response = model.generate_content(f"""Article title: {title}
Article content: {content}

1. Write a 2-sentence summary.
2. Classify into ONE category: [Detection, Misuse, Legislation, Research, Other]

Respond in this format:
SUMMARY: ...
CATEGORY: ...""")
    return response.text
