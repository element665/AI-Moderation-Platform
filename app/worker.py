import os

import requests

from app.queue import dequeue_comment, enqueue_comment
from app.classifier import classify
from app.rules import apply_rules
from app.actions import send_alert
from app.db import save_comment, init_db
from app.logging_utils import get_logger, log_event

logger = get_logger(__name__)
MAX_RETRIES = 3
SLACK_URL = os.getenv("SLACK_WEBHOOK_URL")


def _send_permanent_failure_alert(comment, error):
    if not SLACK_URL:
        return

    payload = {
        "text": "❌ Failed permanently after retries",
        "attachments": [
            {
                "text": comment.get("text"),
                "fields": [
                    {"title": "Platform", "value": comment.get("platform", "unknown")},
                    {"title": "Error", "value": str(error)},
                ],
            }
        ],
    }
    requests.post(SLACK_URL, json=payload)

def run_worker():
    init_db()

    while True:
        comment = dequeue_comment()
        retry_count = comment.get("retry_count", 0)
        log_event(
            logger,
            "comment_processing_started",
            platform=comment.get("platform", "unknown"),
            retry_count=retry_count,
        )

        try:
            result = classify(comment["text"])
            action = apply_rules(result)
            log_event(logger, "action_decided", action=action, label=result.get("label"))

            if action.startswith("alert"):
                send_alert(comment, result)

            save_comment(comment, result)
            log_event(
                logger,
                "comment_processing_completed",
                platform=comment.get("platform", "unknown"),
                action=action,
                retry_count=retry_count,
            )
        except Exception as exc:
            if retry_count < MAX_RETRIES:
                comment["retry_count"] = retry_count + 1
                log_event(
                    logger,
                    "comment_processing_retry",
                    retry_attempt=comment["retry_count"],
                    max_retries=MAX_RETRIES,
                    reason=str(exc),
                    platform=comment.get("platform", "unknown"),
                )
                enqueue_comment(comment)
                continue

            log_event(
                logger,
                "comment_processing_dead_letter",
                retry_count=retry_count,
                max_retries=MAX_RETRIES,
                reason=str(exc),
                platform=comment.get("platform", "unknown"),
            )

            try:
                _send_permanent_failure_alert(comment, exc)
            except Exception as alert_exc:
                log_event(logger, "permanent_failure_alert_failed", reason=str(alert_exc))

            try:
                save_comment(
                    comment,
                    {
                        "label": "failed",
                        "confidence": 0.0,
                    },
                )
            except Exception as db_exc:
                log_event(logger, "permanent_failure_save_failed", reason=str(db_exc))
