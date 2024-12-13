from pydantic import BaseModel
from datetime import datetime


class TagCreate(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
