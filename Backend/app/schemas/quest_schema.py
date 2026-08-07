from pydantic import BaseModel
from typing import Optional

class QuestCreate(BaseModel):
    title: str
    description: Optional[str] = None
    course: Optional[str] = None
    xp_reward: Optional[int] = 10

class QuestResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    course: Optional[str] = None
    completed: bool
    xp_reward: int
    user_id: Optional[int] = None

    class Config:
        from_attributes = True