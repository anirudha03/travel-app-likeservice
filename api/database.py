from pymongo import MongoClient, ASCENDING
from .config import MONGO_URI, DB_NAME, LIKES_COLLECTION

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Ensure unique (post_id, user_id) pair
db[LIKES_COLLECTION].create_index(
    [("post_id", ASCENDING), ("user_id", ASCENDING)],
    unique=True
)
