from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from movie.database import engine, Base, SessionLocal
from movie.models import Movies
from movie.schemas import Movie, DisplayMovie

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movie", response_model=list[DisplayMovie])
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.query(Movies).all()
    return movies


@app.get("/movie/{movie_id}", response_model=DisplayMovie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movies).filter(Movies.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post("/movie")
def add_movie(movie: Movie, db: Session = Depends(get_db)):
    new_movie = Movies(title=movie.title, year=movie.year, genre=movie.genre)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return movie


@app.put("/movie/{movie_id}")
def update_movie(movie: Movie, movie_id: int, db: Session = Depends(get_db)):
    movie1 = db.query(Movies).filter(Movies.id == movie_id)
    if not movie1.first():
        raise HTTPException(status_code=404, detail="Movie doesn't exist")

    movie1.update({"title": movie.title, "year": movie.year, "genre": movie.genre})
    db.commit()
    return {"Movie successfully updated"}


@app.delete("/movie/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db.query(Movies).filter(Movies.id == movie_id).delete(synchronize_session=False)
    db.commit()
    return {"detail": "Movie deleted"}


# @app.post("/genre")
# def add_genre(genre: Genre, db: Session = Depends(get_db)):
#     new_genre = Genres(name=genre.name)
#     db.add(new_genre)
#     db.commit()
#     db.refresh(new_genre)
#     return genre
