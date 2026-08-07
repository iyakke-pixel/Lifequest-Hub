from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.stash import Stash
from app.schemas.stash_schema import StashCreate, StashResponse

router = APIRouter(prefix="/api/stashes", tags=["Stash / Loot Vault"])

@router.post("/", response_model=StashResponse)
def create_stash(stash: StashCreate, user_id: int = 1, db: Session = Depends(get_db)):
    db_stash = Stash(**stash.model_dump(), user_id=user_id)
    db.add(db_stash)
    db.commit()
    db.refresh(db_stash)
    return db_stash

@router.get("/", response_model=List[StashResponse])
def get_stashes(user_id: int = 1, db: Session = Depends(get_db)):
    return db.query(Stash).filter(Stash.user_id == user_id).all()

@router.patch("/{stash_id}/deposit", response_model=StashResponse)
def deposit_stash(stash_id: int, amount: float = 25.0, db: Session = Depends(get_db)):
    db_stash = db.query(Stash).filter(Stash.id == stash_id).first()
    if not db_stash:
        raise HTTPException(status_code=404, detail="Stash not found")
    db_stash.current_amount += amount
    db.commit()
    db.refresh(db_stash)
    return db_stash