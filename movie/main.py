from fastapi import FastAPI

from movie.database import engine, Base
from movie.schemas import Movie

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/movie")
def index():
    return "This is a simple movie app"


@app.post("/movie")
def add_movie(movie: Movie):
    return movie
