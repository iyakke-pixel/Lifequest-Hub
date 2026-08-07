from pydantic import BaseModel
from typing import Optional

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    paid_by: str

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    paid_by: str
    is_settled: bool
    user_id: Optional[int] = None

    class Config:
        from_attributes = True