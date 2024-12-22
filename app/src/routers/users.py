from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..domain.auth.schemas import TokenData
from ..domain.user import schemas
from ..dependencies import get_db, get_current_user
from ..domain.user import service
from ..internal.admin import user_dependency

router = APIRouter(prefix="/user", tags=["User"])
user_dependency = Depends(get_current_user)
db_dependency = Depends(get_db)


@router.post("/signup", response_model=schemas.UserView)
def signup(user: schemas.UserCreate, db: Session = db_dependency):
    db_user = service.get_user_by_username(db, user.username)
    if db_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    return service.create_user(db, user)


@router.get("/me", response_model=schemas.UserView)
def get_my_details(current_user: TokenData = user_dependency, db: Session = db_dependency):
    return service.get_user_by_id(db, current_user.sub)


@router.put("/me", response_model=schemas.UserView)
def update_user(updated_user: schemas.UserBase, user: TokenData = user_dependency,
                db: Session = db_dependency):
    db_user = service.update_user(db, user, updated_user)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.post("/change-password")
def change_password(password_request: schemas.UserUpdatePassword, user: TokenData = user_dependency,
                    db: Session = db_dependency):
    db_user = service.update_password(password_request, user, db)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": "Password has been changed successfully"}


@router.delete("/deactivate")
def deactivate_account(current_user: TokenData = user_dependency, db: Session = db_dependency):
    if service.deactivate_account(db, current_user):
        return {"detail": "Account has been deactivated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
