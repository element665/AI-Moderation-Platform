@router.post("/webhook/meta")
async def meta_webhook(payload: dict):
    await queue_producer.send("comments", payload)
    return {"status": "ok"}