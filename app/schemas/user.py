from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    age: int
    gender: str

class UserResponse(UserCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True