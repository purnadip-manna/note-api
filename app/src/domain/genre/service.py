from sqlalchemy.orm import Session
from . import models, schemas


def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Genres).offset(skip).limit(limit).all()


def get_genre_by_id(db: Session, genre_id: int):
    return db.query(models.Genres).filter(models.Genres.id == genre_id).first()


def create_genre(db: Session, genre: schemas.GenreCreate):
    genre_dict = genre.model_dump()

    db_genre = models.Genres(name=genre_dict["name"])

    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre
