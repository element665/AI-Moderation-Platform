from fastapi import FastAPI, Request
from app.logging_utils import get_logger, log_event
from app.queue import enqueue_comment

app = FastAPI()
logger = get_logger(__name__)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    comment = {
        "platform": payload.get("platform", "unknown"),
        "text": payload.get("text"),
        "user": payload.get("user", "anon"),
    }

    log_event(
        logger,
        "comment_ingested",
        platform=comment["platform"],
        user=comment["user"],
        has_text=bool(comment["text"]),
    )
    enqueue_comment(comment)
    return {"queued": True}
