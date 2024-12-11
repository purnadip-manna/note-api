from sqlalchemy.orm import Session
from . import models, schemas
from ...utility import hash_password


def get_user(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    print(user.model_dump_json())
    db_user = models.Users(
        username=user.username,
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        is_active=True,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
