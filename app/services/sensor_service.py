from sqlalchemy.orm import Session
from app.models.sensor import Sensor

def create_sensor(db: Session, temperature: float, humidity: float):
    status = "normal"
    if humidity < 65:
        status = "dry"

    data = Sensor(
        temperature=temperature,
        humidity=humidity,
        status=status
    )

    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def get_all_sensors(db: Session):
    return db.query(Sensor).all()


def get_latest_sensor(db: Session):
    return db.query(Sensor).order_by(Sensor.id.desc()).first()