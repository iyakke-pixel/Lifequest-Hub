from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/user", tags=["User"])

@router.get("/me")
def get_user_profile(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        return {"error": "User not found"}

    today = date.today()

    # If last login was yesterday -> Increment Streak!
    if user.last_login == today - timedelta(days=1):
        user.streak += 1
        user.last_login = today
        db.commit()

    # If last login was today -> Already counted for today
    elif user.last_login == today:
        pass

    # If missed 1 or more days -> Reset Streak to 1
    else:
        user.streak = 1
        user.last_login = today
        db.commit()

    return {
        "username": user.username,
        "email": user.email,
        "xp": user.xp,
        "level": user.level,
        "streak": user.streak
    }