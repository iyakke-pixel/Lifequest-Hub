from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.quest import Quest
from app.models.user import User
from app.schemas.quest_schema import QuestCreate, QuestResponse

router = APIRouter(prefix="/api/quests", tags=["Quests"])

# 1. GET ALL QUESTS
@router.get("/", response_model=List[QuestResponse])
def get_quests(db: Session = Depends(get_db)):
    return db.query(Quest).all()

# 2. CREATE A NEW QUEST
@router.post("/", response_model=QuestResponse)
def create_quest(quest_data: QuestCreate, db: Session = Depends(get_db)):
    new_quest = Quest(
        title=quest_data.title,
        course=quest_data.course,
        xp_reward=quest_data.xp_reward
    )
    db.add(new_quest)
    db.commit()
    db.refresh(new_quest)
    return new_quest

# 3. COMPLETE A QUEST (FIXED 404 HANDLING)
@router.post("/{quest_id}/complete")
def complete_quest(quest_id: int, db: Session = Depends(get_db)):
    # Find the quest by ID
    quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if not quest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Quest not found"
        )
    
    # Get primary user (or auto-create one if database is empty)
    user = db.query(User).first()
    if not user:
        user = User(
            username="Student Scholar", 
            email="student@university.edu", 
            hashed_password="defaultpassword", 
            xp=0, 
            level=1
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    # Award XP and check for level-up
    user.xp = (user.xp or 0) + quest.xp_reward
    if user.xp >= 500:
        user.level = (user.level or 1) + (user.xp // 500)
        user.xp = user.xp % 500
        
    # Delete the completed quest from active list
    db.delete(quest)
    db.commit()
    
    return {
        "message": "Quest completed!", 
        "xp": user.xp, 
        "level": user.level
    }