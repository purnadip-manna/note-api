from sqlalchemy.orm import Session
from . import models, schemas
from ..auth.schemas import TokenData


def get_tags(db: Session, current_user: TokenData, skip: int = 0, limit: int = 10):
    return db.query(models.Tags).filter(models.Tags.created_by == current_user.sub).offset(skip).limit(limit).all()


def get_tag_by_id(db: Session, current_user: TokenData, tag_id: int):
    return db.query(models.Tags).filter(models.Tags.id == tag_id).filter(
        models.Tags.created_by == current_user.sub).first()


def create_tag(db: Session, current_user: TokenData, tag: schemas.TagCreate):
    tag_dict = tag.model_dump()

    db_tag = models.Tags(**tag_dict, created_by=current_user.sub, updated_by=current_user.sub)

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: int, current_user: TokenData):
    db_tag = get_tag_by_id(db, current_user, tag_id)
    if db_tag:
        db.delete(db_tag)
        db.commit()
