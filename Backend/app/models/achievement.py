from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)       # e.g., "Night Owl"
    description = Column(String, nullable=False) # e.g., "Complete a quest after 10 PM"
    icon = Column(String, default="🏆")
    is_unlocked = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)