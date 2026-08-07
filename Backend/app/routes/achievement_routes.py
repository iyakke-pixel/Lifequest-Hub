from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.achievement import Achievement

router = APIRouter(prefix="/api/achievements", tags=["Achievements"])

# Default badges setup
DEFAULT_BADGES = [
    {"title": "First Step", "description": "Complete your first quest", "icon": "⚔️"},
    {"title": "Streak Master", "description": "Reach a 3-day login streak", "icon": "🔥"},
    {"title": "Centurion", "description": "Save $100 in the Vault", "icon": "💰"},
    {"title": "Boss Slayer", "description": "Defeat an exam boss", "icon": "👹"}
]

@router.get("/")
def get_achievements(db: Session = Depends(get_db)):
    achievements = db.query(Achievement).all()
    
    # Auto-seed default badges if database is empty
    if not achievements:
        for badge in DEFAULT_BADGES:
            db.add(Achievement(**badge, is_unlocked=False))
        db.commit()
        achievements = db.query(Achievement).all()

    return achievements