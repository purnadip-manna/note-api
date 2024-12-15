from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_user
from ..domain.auth.schemas import TokenData
from ..domain.tag import schemas
from ..domain.tag import service

router = APIRouter(prefix="/tag", tags=["Tag"])

user_dependency = Depends(get_current_user)
db_dependency = Depends(get_db)


@router.get("/", response_model=list[schemas.TagResponse])
def get_tags(
        skip: int = 0,
        limit: int = 10,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency,
):
    return service.get_tags(db, current_user, skip, limit)


@router.get("/{tag_id}", response_model=schemas.TagResponse)
def get_tag_by_id(
        tag_id: int,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency
):
    db_tag = service.get_tag_by_id(db, current_user, tag_id)
    if db_tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found"
        )
    return db_tag


@router.post(
    "/", response_model=schemas.TagResponse, status_code=status.HTTP_201_CREATED
)
def create_tag(
        tag: schemas.TagCreate,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency,
):
    return service.create_tag(db, current_user, tag)

@router.delete("/{tag_id}")
def delete_tag(
        tag_id: int,
        current_user: TokenData = user_dependency,
        db: Session = db_dependency
):
    service.delete_tag(db, tag_id, current_user)
    return {"detail": "Tag deleted"}