from fastapi import FastAPI, HTTPException

from app.database import (
    create_tables,
    get_all_daily_reports,
    get_daily_report_by_id,
    insert_daily_report,
)
from app.models import DailyReportCreate

app = FastAPI(
    title="Daily Report API",
    description="Level 1 Foundation project for learning API, JSON, database, Git, and Docker.",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup() -> None:
    create_tables()


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Daily Report API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "daily-report-api",
    }


@app.post("/reports", status_code=201)
def create_report(report: DailyReportCreate) -> dict:
    report_data = report.model_dump()
    report_id = insert_daily_report(report_data)

    return {
        "message": "Report created",
        "data": {
            "id": report_id,
            **report_data,
        },
    }


@app.get("/reports")
def list_reports() -> dict:
    reports = get_all_daily_reports()

    return {
        "count": len(reports),
        "data": reports,
    }


@app.get("/reports/{report_id}")
def get_report(report_id: int) -> dict:
    report = get_daily_report_by_id(report_id)

    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return {
        "data": report,
    }
