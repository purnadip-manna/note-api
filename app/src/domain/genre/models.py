from ...database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
# from sqlalchemy.orm import relationship


class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())

    # movies = relationship("Movies", back_populates="genres")
