from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    level: Optional[int] = 1
    xp: Optional[int] = 0
    streak: Optional[int] = 1

    class Config:
        from_attributes = True