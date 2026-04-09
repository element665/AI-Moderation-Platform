import requests
import os

SLACK_URL = os.getenv("SLACK_WEBHOOK_URL")

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

    requests.post(SLACK_URL, json=payload)