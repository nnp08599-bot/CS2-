import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict

DB_PATH = Path("data/db/demos.sqlite3")


class DemoRow(TypedDict):
    id: int
    filename: str
    date_added: str


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with closing(get_connection()) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS demos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                date_added TEXT NOT NULL
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_demos_date_added ON demos(date_added)"
        )
        connection.commit()


def add_demo(filename: str, date_added: str | None = None) -> int:
    added_at = date_added or datetime.now(timezone.utc).isoformat()
    with closing(get_connection()) as connection:
        cursor = connection.execute(
            "INSERT INTO demos (filename, date_added) VALUES (?, ?)",
            (filename, added_at),
        )
        connection.commit()
        return int(cursor.lastrowid)


def list_demos() -> list[DemoRow]:
    with closing(get_connection()) as connection:
        rows = connection.execute(
            "SELECT id, filename, date_added FROM demos ORDER BY id DESC"
        ).fetchall()
    return [DemoRow(id=row["id"], filename=row["filename"], date_added=row["date_added"]) for row in rows]
