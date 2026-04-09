from app.queue import dequeue_comment
from app.classifier import classify
from app.rules import apply_rules
from app.actions import send_alert
from app.db import save_comment, init_db

def run_worker():
    init_db()

    while True:
        comment = dequeue_comment()

        result = classify(comment["text"])
        action = apply_rules(result)

        if action.startswith("alert"):
            send_alert(comment, result)

        save_comment(comment, result)