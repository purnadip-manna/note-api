from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_user
from ..domain.auth.schemas import TokenData
from ..domain.note import schemas
from ..domain.note import service

router = APIRouter(prefix="/note", tags=["Note"])

user_dependency = Depends(get_current_user)
db_dependency = Depends(get_db)


@router.get("/", response_model=list[schemas.NoteResponse])
def get_all_notes(
        skip: int = 0,
        limit: int = 10,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency,
):
    return service.get_notes(db, current_user, skip, limit)


@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note(
        note_id: int, current_user: TokenData = user_dependency, db: Session = db_dependency
):
    db_note = service.get_note_by_id(db, note_id, current_user)
    if db_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )

    return db_note


@router.post(
    "/", response_model=schemas.NoteResponse, status_code=status.HTTP_201_CREATED
)
def add_note(
        note: schemas.NoteCreate,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency,
):
    return service.create_note(db, note, current_user)


@router.put("/{note_id}")
def update_note(note: schemas.NoteCreate, note_id: int, db: Session = db_dependency,
                current_user: TokenData = user_dependency):
    return service.update_note(db, current_user, note_id, note)


@router.delete("/{note_id}")
def delete_note(
        note_id: int,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency
):
    service.delete_note(db, note_id, current_user)
    return {"detail": "Note deleted"}
