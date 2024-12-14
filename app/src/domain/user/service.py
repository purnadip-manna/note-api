from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from . import models, schemas
from ..auth.schemas import TokenData
from ...utility import hash_password, verify_password


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


def update_user(db: Session, user: TokenData, updated_user: schemas.UserBase):
    db_user = db.query(models.Users).filter(models.Users.username == user.sub).first()
    if db_user:
        db_user.name = updated_user.name
        db_user.email = updated_user.email
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None


def update_password(password_request: schemas.UserUpdatePassword, user: TokenData, db: Session):
    if password_request.new_password == password_request.confirm_password:
        db_user = db.query(models.Users).filter(models.Users.username == user.sub).first()
        if db_user:
            if verify_password(password_request.old_password, db_user.password):
                db_user.password = hash_password(password_request.new_password)
                db_user.token_version = db_user.token_version + 1
                db.commit()
                db.refresh(db_user)
                return db_user
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect old password")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")
