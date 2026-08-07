from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.database import Base

class SharedExpense(Base):
    __tablename__ = "shared_expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    paid_by = Column(String, nullable=False)
    is_settled = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)