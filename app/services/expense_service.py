from datetime import date as date_type

from app.db import expense_repository
from app.models.expense import Expense


def add_expense(expense: Expense) -> dict:
    expense_date = expense.date or date_type.today().isoformat()
    return expense_repository.insert_expense(
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        date=expense_date,
    )


def get_summary(category: str = "", start_date: str = "", end_date: str = "") -> dict:
    results = expense_repository.fetch_expenses(category, start_date, end_date)
    return {
        "count": len(results),
        "total_amount": sum(e["amount"] for e in results),
        "expenses": results,
    }

def get_total_exp_for_cat(category: str):
    return expense_repository.get_total_amount_by_category(category)
