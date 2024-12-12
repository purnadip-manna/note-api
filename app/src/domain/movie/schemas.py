from pydantic import BaseModel, Field
from datetime import datetime


class MovieCreate(BaseModel):
    title: str
    year: int = Field(gt=1999, lt=2025)  # Data validation
    genre: str


class MovieResponse(BaseModel):
    id: int
    title: str
    year: int
    genre: str
    created_at: datetime
