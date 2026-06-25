from datetime import date as date_type

from app.db import budget_repository
from app.models.budget import Budget
from app.db import expense_repository


def add_budget(budget: Budget):
    budget_repository.set_budget(
        category = budget.category,
        monthly_limit = budget.monthly_limit,
        updated_date=budget.updated_date
    )
    return "budget added"

def update_budget(budget: Budget):
    updated_date = budget.updated_date or date_type.today().isoformat()
    rows_affected = budget_repository.update_budget(
        category=budget.category,
        monthly_limit=budget.monthly_limit,
        updated_date=updated_date,
    )
    if rows_affected == 0:
        budget_repository.set_budget(
            category=budget.category,
            monthly_limit=budget.monthly_limit,
            updated_date=updated_date,
        )
        return "budget created"
    return "budget updated"

def check_budget_status(category: str) -> dict:
    total_exp = expense_repository.get_total_amount_by_category(category)
    records = budget_repository.fetch_budget(category)
    available_budget = records[0]["monthly_limit"] - total_exp if records else None
    return {
        "Category" : records[0]["category"],
        "Total Budget": records[0]["monthly_limit"],
        "Available Budget": available_budget
       
    }