from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db.connection import init_db
from app.routers.expense_router import router as expense_router
from app.routers.budget_router import router as  budget_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Expense Tracker Service", lifespan=lifespan)
app.include_router(expense_router)
app.include_router(budget_router)


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start_server()
