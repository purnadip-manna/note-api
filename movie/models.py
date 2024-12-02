from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from movie.database import Base


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)

    genres = relationship("Genres", back_populates="movies")


class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    movies = relationship("Movies", back_populates="genres")