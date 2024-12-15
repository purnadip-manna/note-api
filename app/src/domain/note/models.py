from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, UUID
from datetime import datetime

from ...database import Base

timestamp = datetime.now()

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=timestamp)
    created_by = Column(UUID, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=timestamp)
    updated_by = Column(UUID, ForeignKey("users.id"))
