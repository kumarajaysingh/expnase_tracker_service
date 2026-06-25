from fastapi import APIRouter

from app.models.expense import Expense
from app.services import expense_service

router = APIRouter()


@router.post("/api/expense")
def add_expense(expense: Expense):
    return expense_service.add_expense(expense)


@router.get("/api/expense/summary")
def get_summary(category: str = "", start_date: str = "", end_date: str = ""):
    return expense_service.get_summary(category, start_date, end_date)


