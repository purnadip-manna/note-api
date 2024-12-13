from sqlalchemy.orm import Session
from . import schemas, models


def create_note(db: Session, note: schemas.NoteCreate):
    note_dict = note.model_dump()

    db_note = models.Notes(title=note_dict["title"], content=note_dict["content"])

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Notes).offset(skip).limit(limit).all()


def get_note_by_id(db: Session, note_id: int):
    return db.query(models.Notes).filter(models.Notes.id == note_id).first()


def delete_note(db: Session, note_id: int):
    db.query(models.Notes).filter(models.Notes.id == note_id).delete()
