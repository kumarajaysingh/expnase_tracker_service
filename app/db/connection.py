import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "expenses.db"


def init_db() -> None:
    """One-time setup: create the database file and tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT DEFAULT '',
                date TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT UNIQUE NOT NULL,
                monthly_limit REAL NOT NULL,
                updated_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
            """
        )
        conn.commit()
    finally:
        conn.close()


def get_connection() -> sqlite3.Connection:
    """Open a new connection. Callers are responsible for closing it."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
