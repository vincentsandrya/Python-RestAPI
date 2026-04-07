from sqlalchemy.orm import Session
from app.models.user import User

def create(db:Session, username: str, age: int, gender: str):
    user = User(username=username, age=age, gender=gender)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db: Session):
    return db.query(User).all()

def get_single(db: Session, id: int):
    return db.query(User).where(User.id == id).first()

def update(db: Session, id: int, username: str, age: int, gender: str):
    user = db.query(User).where(User.id == id).first()
    user.username = username
    user.age = age
    user.gender = gender
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, id: int):
    user = db.query(User).where(User.id == id).first()
    db.delete(user)
    db.commit()
    return user