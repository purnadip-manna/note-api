from ...database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())
