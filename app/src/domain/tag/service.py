from sqlalchemy.orm import Session
from . import models, schemas


def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tags).offset(skip).limit(limit).all()


def get_tag_by_id(db: Session, tag_id: int):
    return db.query(models.Tags).filter(models.Tags.id == tag_id).first()


def create_tag(db: Session, tag: schemas.TagCreate):
    tag_dict = tag.model_dump()

    db_tag = models.Tags(name=tag_dict["name"])

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
