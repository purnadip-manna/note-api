from pydantic import BaseModel
from typing import List
from datetime import datetime


# class Genre(BaseModel):
#     id: UUID = None
#     name: str


class Movie(BaseModel):
    id: int = None
    title: str
    year: int
    # genre: Set[Genre]
    genre: str
    cast: List[str]
    created_at: datetime
