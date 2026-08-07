from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Boss(Base):
    __tablename__ = "bosses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # e.g., "Organic Chemistry Midterm"
    max_hp = Column(Integer, default=100)
    current_hp = Column(Integer, default=100)
    xp_reward = Column(Integer, default=300)
    is_defeated = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)