from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_user
from ..domain.note import schemas
from ..domain.note import service

router = APIRouter(prefix="/note", tags=["Note"])


@router.get("/", response_model=list[schemas.NoteResponse])
def get_all_notes(
        skip: int = 0,
        limit: int = 10,
        token: dict = Depends(get_current_user),
        db: Session = Depends(get_db),
):
    print("Token Data:")
    print(token)
    return service.get_notes(db, skip, limit)


@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note(
        note_id: int, token: str = Depends(get_current_user), db: Session = Depends(get_db)
):
    db_note = service.get_note_by_id(db, note_id)
    if db_note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )

    return db_note


@router.post(
    "/", response_model=schemas.NoteResponse, status_code=status.HTTP_201_CREATED
)
def add_note(
        note: schemas.NoteCreate,
        token: str = Depends(get_current_user),
        db: Session = Depends(get_db),
):
    return service.create_note(db, note)


# @router.put("/{note_id}")
# def update_note(note: schemas, note_id: int, db: Session = Depends(get_db)):
#     note1 = db.query(Movies).filter(Movies.id == note_id)
#     if not note1.first():
#         raise HTTPException(status_code=404, detail="Movie doesn't exist")

#     note1.update({"title": note.title, "year": note.year, "tag": note.tag})
#     db.commit()
#     return {"Movie successfully updated"}


@router.delete("/{note_id}")
def delete_note(
        note_id: int, token: str = Depends(get_current_user), db: Session = Depends(get_db)
):
    service.delete_note(db, note_id)
    return {"detail": "Movie deleted"}
