from pydantic import BaseModel
from typing import Optional

class StashCreate(BaseModel):
    name: str
    target_amount: float

class StashResponse(BaseModel):
    id: int
    name: str
    target_amount: float
    current_amount: float
    user_id: Optional[int] = None

    class Config:
        from_attributes = True