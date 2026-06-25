from typing import List, Optional

from app.db.connection import get_connection


def insert_expense(amount: float, category: str, description: str, date: str) -> dict:
    conn = get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
            (amount, category, description, date),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM expenses WHERE id = ?", (cursor.lastrowid,)
        ).fetchone()
        return dict(row)
    finally:
        conn.close()


def fetch_expenses(
    category: Optional[str] = "",
    start_date: Optional[str] = "",
    end_date: Optional[str] = "",
) -> List[dict]:
    conn = get_connection()
    try:
        query = "SELECT * FROM expenses WHERE 1=1"
        params: list = []
        if category:
            query += " AND LOWER(category) = LOWER(?)"
            params.append(category)
        if start_date:
            query += " AND date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND date <= ?"
            params.append(end_date)

        rows = conn.execute(query, params).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


def get_total_amount_by_category(category: str) -> float:
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses WHERE LOWER(category) = LOWER(?)",
            (category,),
        ).fetchone()
        return row["total"]
    finally:
        conn.close()
