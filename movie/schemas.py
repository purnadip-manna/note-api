from pydantic import BaseModel
from uuid import UUID
from typing import List, Set
from datetime import datetime


class Genre(BaseModel):
    id: UUID = None
    name: str

class Movie(BaseModel):
    id: UUID = None
    title: str
    year: int
    genre: Set[Genre]
    cast: List[str]
    created_at: datetime