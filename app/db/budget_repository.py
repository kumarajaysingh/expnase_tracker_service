
from app.db.connection import get_connection

def set_budget(category: str, monthly_limit: float, updated_date: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "insert into budgets (category, monthly_limit, updated_date) values (?, ? , ?)",
            (category, monthly_limit, updated_date)
        )

        conn.commit()
    finally:
        conn.close()

def update_budget(category: str, monthly_limit: float, updated_date: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "update budgets set monthly_limit = ?, updated_date = ? where category = ?",
            (monthly_limit, updated_date, category),
        )
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()

def fetch_budget(category: str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    try:
        rows = cursor.execute(
            "select category, monthly_limit from budgets where category=?", (category,)
        ).fetchall()
        
        return [dict(row) for row in rows]
    finally:
        conn.close()