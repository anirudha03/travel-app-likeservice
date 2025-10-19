import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "travel_app")
# Mongo collections
LIKES_COLLECTION = "likes"
POSTS_COLLECTION = "posts"

RABBITMQ_URL = os.getenv(
    "RABBITMQ_URL",
    "null"
)
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = "like_queue"
