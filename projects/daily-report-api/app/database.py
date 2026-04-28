import os
import sqlite3
from typing import Any

DATABASE_NAME = os.getenv("DATABASE_NAME", "app.db")


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables() -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            farm_name TEXT NOT NULL,
            population INTEGER NOT NULL,
            mortality INTEGER NOT NULL,
            feed_used_kg REAL NOT NULL,
            average_weight REAL NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def insert_daily_report(report: dict[str, Any]) -> int:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO daily_reports (
            date,
            farm_name,
            population,
            mortality,
            feed_used_kg,
            average_weight
        ) VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            report["date"],
            report["farm_name"],
            report["population"],
            report["mortality"],
            report["feed_used_kg"],
            report["average_weight"],
        ),
    )

    connection.commit()
    report_id = cursor.lastrowid
    connection.close()

    return int(report_id)


def get_all_daily_reports() -> list[dict[str, Any]]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM daily_reports ORDER BY id DESC")
    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]


def get_daily_report_by_id(report_id: int) -> dict[str, Any] | None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM daily_reports WHERE id = ?", (report_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return dict(row)
