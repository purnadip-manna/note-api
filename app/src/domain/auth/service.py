from sqlalchemy.orm import Session

from ..user.service import get_user_by_username
from ...utility import verify_password


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
