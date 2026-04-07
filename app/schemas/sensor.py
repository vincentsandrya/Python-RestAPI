from pydantic import BaseModel
from datetime import datetime

class SensorCreate(BaseModel):
    temperature: float
    humidity: float

class SensorResponse(SensorCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True