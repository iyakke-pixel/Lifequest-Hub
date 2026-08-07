from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/leaderboard", tags=["Leaderboard"])

@router.get("/")
def get_leaderboard(db: Session = Depends(get_db)):
    # Fetch top 10 users ordered by Level and XP
    top_users = (
        db.query(User)
        .order_by(User.level.desc(), User.xp.desc())
        .limit(10)
        .all()
    )
    
    return [
        {
            "username": user.username,
            "level": user.level,
            "xp": user.xp,
            "streak": getattr(user, "streak", 1)
        }
        for user in top_users
    ]