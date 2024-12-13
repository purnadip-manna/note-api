from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .utility import verify_password
import jwt

from .domain.user.models import Users
from .config import SECRET_KEY, ALGORITHM

oauth_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(token: str = Depends(oauth_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

        token_data = {"username": username}
        return token_data

    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
