from fastapi import APIRouter, HTTPException
from api.models import LikeRequest, UnlikeRequest
from api.config import RABBITMQ_URL, RABBITMQ_QUEUE
import pika
import json

router = APIRouter()

def get_channel():
    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    return connection, channel

@router.post("/like")
async def like_post(request: LikeRequest):
    try:
        connection, channel = get_channel()
        message = json.dumps({"action": "like", **request.dict()})
        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        connection.close()
        return {"status": "queued", "message": "Like event queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/unlike")
async def unlike_post(request: UnlikeRequest):
    try:
        connection, channel = get_channel()
        message = json.dumps({"action": "unlike", **request.dict()})
        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        connection.close()
        return {"status": "queued", "message": "Unlike event queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))