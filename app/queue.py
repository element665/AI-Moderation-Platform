# app/queue.py
import redis
import json
import os

r = redis.Redis.from_url(os.getenv("REDIS_URL"))

QUEUE_NAME = "comments"

def enqueue_comment(comment):
    r.lpush(QUEUE_NAME, json.dumps(comment))

def dequeue_comment():
    _, data = r.brpop(QUEUE_NAME)
    return json.loads(data)