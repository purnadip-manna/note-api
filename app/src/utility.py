import jwt
from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .domain.auth.schemas import TokenData
from .domain.user.models import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: Users):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = dict()
    payload["sub"] = str(data.id)
    payload["name"] = data.name
    payload["email"] = data.email
    payload["role"] = data.role
    payload["token_version"] = data.token_version
    payload["exp"] = expire

    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def has_authority(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_user: TokenData = args[0]
            if current_user.role == role:
                return func(*args, **kwargs)
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                    detail="You do not have permission to access this.")

        return wrapper

    return decorator
