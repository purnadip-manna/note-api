from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
# from sqlalchemy.orm import relationship

from ...database import Base


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    # genres = relationship("Genres", back_populates="movies")
