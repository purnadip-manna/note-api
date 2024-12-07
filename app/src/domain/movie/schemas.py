from pydantic import BaseModel
from datetime import datetime


class MovieCreate(BaseModel):
    title: str
    year: int
    genre: str


class MovieResponse(BaseModel):
    id: int
    title: str
    year: int
    genre: str
    created_at: datetime
