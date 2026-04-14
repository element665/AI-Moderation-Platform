from app.queue import dequeue_comment
from app.classifier import classify
from app.rules import apply_rules
from app.actions import send_alert
from app.db import save_comment, init_db
from app.logging_utils import get_logger, log_event

logger = get_logger(__name__)

def run_worker():
    init_db()

    while True:
        comment = dequeue_comment()
        log_event(logger, "comment_processing_started", platform=comment["platform"])

        result = classify(comment["text"])
        action = apply_rules(result)
        log_event(logger, "action_decided", action=action, label=result.get("label"))

        if action.startswith("alert"):
            send_alert(comment, result)

        save_comment(comment, result)
        log_event(logger, "comment_processing_completed", platform=comment["platform"], action=action)
