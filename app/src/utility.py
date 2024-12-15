import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
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
    payload["token_version"] = data.token_version
    payload["exp"] = expire

    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
