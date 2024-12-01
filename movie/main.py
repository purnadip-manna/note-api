from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from database import engine, SessionLocal
from schemas import Movie
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/movie")
def index():
    return "This is a simple movie app"


@app.post("/movie")
def add_movie(movie: Movie):
    return movie
