from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from . import schemas, models
from ..auth.schemas import TokenData
from ..tag.service import get_tag_by_name


def create_note(db: Session, note: schemas.NoteCreate, current_user: TokenData):
    db_note = models.Notes(
        title=note.title,
        content=note.content,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        created_by=current_user.sub,
        updated_by=current_user.sub
    )

    if note.tags:
        if len(note.tags) != 0:
            for tag in note.tags:
                db_tag = get_tag_by_name(db, current_user, tag)
                if db_tag:
                    db_note.tags.append(db_tag)
                else:
                    raise HTTPException(status_code=400, detail="Tag doesn't exist. Try with proper tag name.")

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes(db: Session, current_user: TokenData, skip: int = 0, limit: int = 10):
    return db.query(models.Notes).filter(models.Notes.created_by == current_user.sub).offset(skip).limit(limit).all()


def get_note_by_id(db: Session, note_id: int, current_user: TokenData):
    return db.query(models.Notes).filter(models.Notes.id == note_id).filter(
        models.Notes.created_by == current_user.sub).first()


def update_note(db: Session, current_user: TokenData, note_id: int, note: schemas.NoteCreate):
    db_note = get_note_by_id(db, note_id, current_user)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note doesn't exist")

    db_note.tags = []
    if note.tags:
        if len(note.tags) != 0:
            for tag in note.tags:
                db_tag = get_tag_by_name(db, current_user, tag)
                if db_tag:
                    db_note.tags.append(db_tag)
                else:
                    raise HTTPException(status_code=400, detail="Tag doesn't exist. Try with proper tag name.")

    db_note.title = note.title
    db_note.content = note.content
    db_note.updated_by = current_user.sub
    db_note.updated_at = datetime.now()

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int, current_user: TokenData):
    db_note = get_note_by_id(db, note_id, current_user)
    if db_note:
        db.delete(db_note)
        db.commit()
