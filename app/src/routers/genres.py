from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..domain.genre import schemas
from ..domain.genre import service
from ..dependencies import get_db

router = APIRouter(prefix="/genre", tags=["Genre"])


@router.get("/", response_model=list[schemas.GenreResponse])
def get_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_genres(db, skip, limit)


@router.get("/{genre_id}", response_model=schemas.GenreResponse)
def get_genre_by_id(genre_id: int, db: Session = Depends(get_db)):
    db_genre = service.get_genre_by_id(db, genre_id)
    if db_genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found"
        )
    return db_genre


@router.post(
    "/", response_model=schemas.GenreResponse, status_code=status.HTTP_201_CREATED
)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return service.create_genre(db, genre)
