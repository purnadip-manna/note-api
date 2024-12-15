from pydantic import BaseModel, UUID4
from datetime import datetime


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_by: UUID4
    created_at: datetime
    updated_by: UUID4
    updated_at: datetime
