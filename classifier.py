import anthropic

client = anthropic.Anthropic()

def classify_article(title, content):
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"""Article title: {title}
Article content: {content}

1. Write a 2-sentence summary.
2. Classify into ONE category: [Detection, Misuse, Legislation, Research, Other]

Respond in this format:
SUMMARY: ...
CATEGORY: ..."""
        }]
    )
    return message.content[0].text
