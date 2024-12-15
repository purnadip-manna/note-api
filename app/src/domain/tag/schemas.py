from pydantic import BaseModel, UUID4
from datetime import datetime


class TagCreate(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: int
    name: str
    created_by: UUID4
    created_at: datetime
    updated_by: UUID4
    updated_at: datetime
