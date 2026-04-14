import json
import os

from openai import OpenAI
from app.logging_utils import get_logger, log_event

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logger = get_logger(__name__)

def classify(text: str):
    log_event(logger, "classification_started", text_length=len(text or ""))

    if os.getenv("USE_MOCK_CLASSIFIER", "false").lower() == "true":
        normalized_text = (text or "").lower()

        if any(word in normalized_text for word in ["scam", "garbage", "fake", "spam"]):
            result = {"label": "toxic", "confidence": 0.9, "reason": "mock classifier"}
        elif any(word in normalized_text for word in ["buy", "http", "link"]):
            result = {"label": "spam", "confidence": 0.85, "reason": "mock classifier"}
        else:
            result = {"label": "neutral", "confidence": 0.8, "reason": "mock classifier"}

        log_event(
            logger,
            "classification_completed",
            label=result.get("label"),
            confidence=result.get("confidence"),
        )
        return result

    prompt = f"""
    Classify this comment as spam, toxic, or neutral.
    Return JSON with label, confidence, and reason.

    Comment: "{text}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content or ""

    if content.startswith("```"):
        lines = content.splitlines()
        if len(lines) >= 3:
            content = "\n".join(lines[1:-1]).strip()

    try:
        result = json.loads(content)
        log_event(
            logger,
            "classification_completed",
            label=result.get("label"),
            confidence=result.get("confidence"),
        )
        return result
    except json.JSONDecodeError as exc:
        log_event(logger, "classification_failed", error=str(exc))
        raise ValueError(f"Classifier returned invalid JSON: {content}") from exc
