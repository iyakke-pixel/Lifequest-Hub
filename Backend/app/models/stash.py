from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Stash(Base):
    __tablename__ = "stashes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    target_amount = Column(Float, nullable=False)
    current_amount = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)