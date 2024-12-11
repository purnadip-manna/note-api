from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..domain.user import schemas
from ..dependencies import get_db
from ..domain.user import service

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user(db, user.username)
    if db_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    return service.create_user(db, user)
