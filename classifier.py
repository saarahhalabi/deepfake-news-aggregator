from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def classify_article(title, content):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""Article title: {title}
Article content: {content}

1. Write a 2-sentence summary.
2. Classify into ONE category: [Detection, Misuse, Legislation, Research, Other]

Respond in this format:
SUMMARY: ...
CATEGORY: ..."""
    )
    return response.text
