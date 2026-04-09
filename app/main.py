# app/main.py
from fastapi import FastAPI, Request
from app.queue import enqueue_comment

app = FastAPI()

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

    enqueue_comment(comment)
    return {"queued": True}