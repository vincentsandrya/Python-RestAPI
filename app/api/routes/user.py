from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, data.username, data.age, data.gender)


@router.get("/", response_model=list[UserResponse])
def get_all(db: Session = Depends(get_db)):
    return user_service.get_all(db)


@router.get("/{id}", response_model=UserResponse)
def get_single(id: int, db: Session = Depends(get_db)):
    return user_service.get_single(db, id)
    
@router.put("/{id}", response_model=UserResponse)
def update(id: int, data: UserCreate, db: Session = Depends(get_db)):
    return user_service.update(db, id, data.username, data.age, data.gender)

# @router.put("/{id}", response_model=UserResponse)
# def update(data: UserCreate, id: int, db: Session = Depends(get_db)):
#     return user_service.update(db, id)

@router.delete("/{id}", response_model=UserResponse)
def delete(id: int, db: Session = Depends(get_db)):
    return user_service.delete(db, id)