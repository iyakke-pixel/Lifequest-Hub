from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from datetime import date
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Gamification & Finance fields
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    streak = Column(Integer, default=1)
    savings = Column(Float, default=0.0)
    last_login = Column(Date, default=date.today)