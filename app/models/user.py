from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "tb_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)