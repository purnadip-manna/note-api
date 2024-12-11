from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..domain.movie import schemas
from ..domain.movie import service
from ..dependencies import get_db


router = APIRouter(prefix="/movie", tags=["Movie"])

oauth_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


@router.get("/", response_model=list[schemas.MovieResponse])
def get_all_movies(
    skip: int = 0,
    limit: int = 10,
    token: str = Depends(oauth_scheme),
    db: Session = Depends(get_db),
):
    return service.get_movies(db, skip, limit)


@router.get("/{movie_id}", response_model=schemas.MovieResponse)
def get_movie(
    movie_id: int, token: str = Depends(oauth_scheme), db: Session = Depends(get_db)
):
    db_movie = service.get_movie_by_id(db, movie_id)
    if db_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )

    return db_movie


@router.post(
    "/", response_model=schemas.MovieResponse, status_code=status.HTTP_201_CREATED
)
def add_movie(
    movie: schemas.MovieCreate,
    token: str = Depends(oauth_scheme),
    db: Session = Depends(get_db),
):
    return service.create_movie(db, movie)


# @router.put("/{movie_id}")
# def update_movie(movie: schemas, movie_id: int, db: Session = Depends(get_db)):
#     movie1 = db.query(Movies).filter(Movies.id == movie_id)
#     if not movie1.first():
#         raise HTTPException(status_code=404, detail="Movie doesn't exist")

#     movie1.update({"title": movie.title, "year": movie.year, "genre": movie.genre})
#     db.commit()
#     return {"Movie successfully updated"}


@router.delete("/{movie_id}")
def delete_movie(
    movie_id: int, token: str = Depends(oauth_scheme), db: Session = Depends(get_db)
):
    service.delete_movie(db, movie_id)
    return {"detail": "Movie deleted"}
