from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/finance", tags=["Finance"])

class AmountRequest(BaseModel):
    amount: float

class ExpenseRequest(BaseModel):
    title: str
    amount: float
    split_with: str

# 1. Savings Deposit / Withdraw
@router.post("/savings/deposit")
def deposit_savings(data: AmountRequest, db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update savings balance (assuming user model has savings field or default)
    user.savings = getattr(user, 'savings', 0.0) + data.amount
    db.commit()
    return {"message": "Deposit successful", "savings": user.savings}

@router.post("/savings/withdraw")
def withdraw_savings(data: AmountRequest, db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    current_savings = getattr(user, 'savings', 0.0)
    if current_savings < data.amount:
        raise HTTPException(status_code=400, detail="Insufficient savings")
        
    user.savings = current_savings - data.amount
    db.commit()
    return {"message": "Withdrawal successful", "savings": user.savings}

# 2. Shared Expenses
@router.post("/expenses/settle")
def settle_expense(data: AmountRequest, db: Session = Depends(get_db)):
    return {"message": f"Settled expense of ${data.amount:.2f}"}