from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import UUID4
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_user
from ..domain.auth.schemas import TokenData
from ..domain.user import schemas
from ..domain.user import service

router = APIRouter(prefix="/admin", tags=["Admin"])
user_dependency = Depends(get_current_user)
db_dependency = Depends(get_db)


@router.get("/users", response_model=list[schemas.UserView])
def get_all_users(db: Session = db_dependency, current_user: TokenData = user_dependency):
    return service.get_all_users(current_user, db)


@router.put("/users/{user_id}", response_model=schemas.UserView)
def update_user_by_id(user_id: UUID4, updated_user: schemas.UserBase, current_user: TokenData = user_dependency,
                      db: Session = db_dependency):
    db_user = service.update_user_by_id(current_user, db, user_id, updated_user)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: UUID4, current_user: TokenData = user_dependency, db: Session = db_dependency):
    if not service.delete_user_by_id(current_user, db, user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": "User deleted successfully"}
