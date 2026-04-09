# app/classifier.py
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify(text: str):
    prompt = f"""
    Classify this comment as spam, toxic, or neutral.
    Return JSON with label, confidence, and reason.

    Comment: "{text}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content

    # quick & dirty parse (we’ll improve later)
    return eval(content)