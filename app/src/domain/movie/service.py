from sqlalchemy.orm import Session
from . import schemas, models


def create_movie(db: Session, movie: schemas.MovieCreate):
    movie_dict = movie.model_dump()

    db_movie = models.Movies(
        title=movie_dict["title"], year=movie_dict["year"], genre=movie_dict["genre"]
    )

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movies).offset(skip).limit(limit).all()


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movies).filter(models.Movies.id == movie_id).first()


def delete_movie(db: Session, movie_id: int):
    db.query(models.Movies).filter(models.Movies.id == movie_id).delete()
