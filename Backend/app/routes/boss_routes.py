from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app.database import get_db
from app.models.boss import Boss
from app.models.user import User

router = APIRouter(prefix="/api/bosses", tags=["Boss Battles"])

class BossCreate(BaseModel):
    title: str
    max_hp: int = 100
    xp_reward: int = 300

@router.get("/")
def get_bosses(db: Session = Depends(get_db)):
    return db.query(Boss).filter(Boss.is_defeated == False).all()

@router.post("/")
def create_boss(boss_data: BossCreate, db: Session = Depends(get_db)):
    boss = Boss(
        title=boss_data.title,
        max_hp=boss_data.max_hp,
        current_hp=boss_data.max_hp,
        xp_reward=boss_data.xp_reward
    )
    db.add(boss)
    db.commit()
    db.refresh(boss)
    return boss

@router.post("/{boss_id}/attack")
def attack_boss(boss_id: int, damage: int = 25, db: Session = Depends(get_db)):
    boss = db.query(Boss).filter(Boss.id == boss_id).first()
    if not boss or boss.is_defeated:
        raise HTTPException(status_code=404, detail="Active Boss not found")

    boss.current_hp = max(0, boss.current_hp - damage)
    
    # Check if Boss is defeated
    xp_awarded = 0
    if boss.current_hp <= 0:
        boss.is_defeated = True
        xp_awarded = boss.xp_reward
        
        # Award XP to primary user
        user = db.query(User).first()
        if user:
            user.xp = (user.xp or 0) + xp_awarded
            if user.xp >= 500:
                user.level = (user.level or 1) + (user.xp // 500)
                user.xp = user.xp % 500

    db.commit()
    return {
        "current_hp": boss.current_hp,
        "max_hp": boss.max_hp,
        "is_defeated": boss.is_defeated,
        "xp_awarded": xp_awarded
    }