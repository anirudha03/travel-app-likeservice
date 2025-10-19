from pydantic import BaseModel

class LikeRequest(BaseModel):
    post_id: str
    user_id: str

class UnlikeRequest(BaseModel):
    post_id: str
    user_id: str
