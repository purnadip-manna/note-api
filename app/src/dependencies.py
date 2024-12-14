from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
import jwt

from .domain.auth.schemas import TokenData
from .config import SECRET_KEY, ALGORITHM
from .domain.user.models import Users

oauth_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(Users).filter(Users.username == payload.get("sub")).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid authentication credentials")

        if payload.get("sub") is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

        if payload.get("token_version") != user.token_version:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token version mismatch. Please login again.")

        token_data = TokenData(
            sub=payload.get("sub"),
            name=payload.get("name"),
            email=payload.get("email"),
            exp=payload.get("exp")
        )
        return token_data

    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
