from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, UUID, Table
from datetime import datetime

from sqlalchemy.orm import relationship

from ...database import Base

timestamp = datetime.now()

note_tag_table = Table(
    "note_tag",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)


class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    tags = relationship("Tags", secondary=note_tag_table, back_populates="notes")
    created_at = Column(DateTime, default=timestamp)
    created_by = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"))
    updated_at = Column(DateTime, default=timestamp)
    updated_by = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"))
