from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.expense import SharedExpense
from app.schemas.expense_schema import ExpenseCreate, ExpenseResponse

router = APIRouter(prefix="/api/expenses", tags=["Roommate Expenses"])

@router.post("/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = SharedExpense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("/{household_code}", response_model=List[ExpenseResponse])
def get_expenses(household_code: str, db: Session = Depends(get_db)):
    return db.query(SharedExpense).filter(SharedExpense.household_code == household_code).all()