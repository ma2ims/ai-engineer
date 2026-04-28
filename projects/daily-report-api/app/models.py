from pydantic import BaseModel, Field


class DailyReportCreate(BaseModel):
    date: str = Field(..., examples=["2026-04-28"])
    farm_name: str = Field(..., examples=["Tobasa Farm"])
    population: int = Field(..., gt=0, examples=[21000])
    mortality: int = Field(..., ge=0, examples=[35])
    feed_used_kg: float = Field(..., ge=0, examples=[1250])
    average_weight: float = Field(..., ge=0, examples=[1.2])


class DailyReportResponse(DailyReportCreate):
    id: int
