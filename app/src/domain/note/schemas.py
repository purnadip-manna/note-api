from typing import Optional

from pydantic import BaseModel, UUID4
from datetime import datetime

from ..tag.schemas import TagResponse


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: Optional[list[str]] = None


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    tags: Optional[list[TagResponse]]
    created_by: UUID4
    created_at: datetime
    updated_by: UUID4
    updated_at: datetime
