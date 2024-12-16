from sqlalchemy.orm import relationship

from ..note.models import note_tag_table
from ...database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from datetime import datetime

timestamp = datetime.now()


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    notes = relationship("Notes", secondary=note_tag_table, back_populates="tags")
    created_at = Column(DateTime, default=timestamp)
    created_by = Column(UUID, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=timestamp)
    updated_by = Column(UUID, ForeignKey("users.id"))
