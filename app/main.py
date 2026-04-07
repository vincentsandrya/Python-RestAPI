from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.routes import sensor, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensor.router, prefix="/sensor", tags=["Sensor"])
app.include_router(user.router, prefix="/user", tags=["User"])