import os
import requests

from app.logging_utils import get_logger, log_event

SLACK_URL = os.getenv("SLACK_WEBHOOK_URL")
logger = get_logger(__name__)

def send_alert(comment, result):
    payload = {
        "text": f"🚨 {result['label'].upper()} comment detected",
        "attachments": [
            {
                "text": comment["text"],
                "fields": [
                    {"title": "Platform", "value": comment["platform"]},
                    {"title": "Confidence", "value": str(result["confidence"])},
                ],
            }
        ],
    }

    log_event(
        logger,
        "alert_sending",
        platform=comment["platform"],
        label=result["label"],
        confidence=result["confidence"],
    )
    requests.post(SLACK_URL, json=payload)
    log_event(logger, "alert_sent", platform=comment["platform"], label=result["label"])
