from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    course = Column(String, nullable=True)  # <-- Added course column here!
    completed = Column(Boolean, default=False)
    xp_reward = Column(Integer, default=10)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)