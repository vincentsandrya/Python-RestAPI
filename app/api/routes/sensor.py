from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.sensor import SensorCreate, SensorResponse
from app.services import sensor_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SensorResponse)
def create(data: SensorCreate, db: Session = Depends(get_db)):
    return sensor_service.create_sensor(db, data.temperature, data.humidity)


@router.get("/", response_model=list[SensorResponse])
def get_all(db: Session = Depends(get_db)):
    return sensor_service.get_all_sensors(db)


@router.get("/latest", response_model=SensorResponse)
def get_latest(db: Session = Depends(get_db)):
    return sensor_service.get_latest_sensor(db)