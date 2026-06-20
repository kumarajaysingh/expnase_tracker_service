from datetime import date as date_type
from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Expense Tracker Service")

expenses: List[dict] = []
_next_id = 1


class Expense(BaseModel):
    amount: float
    category: str
    description: str = ""
    date: str = ""


@app.post("/api/expense")
def add_expense(expense: Expense):
    global _next_id
    record = expense.model_dump()
    record["id"] = _next_id
    if not record["date"]:
        record["date"] = date_type.today().isoformat()
    _next_id += 1
    expenses.append(record)
    return record


@app.get("/api/expense/summary")
def get_summary(category: str = "", start_date: str = "", end_date: str = ""):
    results = expenses
    if category:
        results = [e for e in results if e["category"].lower() == category.lower()]
    if start_date:
        results = [e for e in results if e["date"] >= start_date]
    if end_date:
        results = [e for e in results if e["date"] <= end_date]

    return {
        "count": len(results),
        "total_amount": sum(e["amount"] for e in results),
        "expenses": results,
    }


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start_server()
