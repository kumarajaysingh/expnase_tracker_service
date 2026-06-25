from fastapi import APIRouter
from app.services import budget_service
from app.models.budget import Budget

router = APIRouter()

@router.post("/api/budget")
def set_budget(budget: Budget):
    return budget_service.add_budget(budget)

@router.get("/api/budget/info")
def get_budget_info(category: str):
    return budget_service.check_budget_status(category)

@router.put("/api/budget/update")
def update_budget(budget: Budget):
    return budget_service.update_budget(budget)