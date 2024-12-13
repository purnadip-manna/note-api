from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..domain.tag import schemas
from ..domain.tag import service
from ..dependencies import get_db

router = APIRouter(prefix="/tag", tags=["Tag"])

oauth_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")


@router.get("/", response_model=list[schemas.TagResponse])
def get_tags(
    skip: int = 0,
    limit: int = 10,
    token: str = Depends(oauth_scheme),
    db: Session = Depends(get_db),
):
    return service.get_tags(db, skip, limit)


@router.get("/{tag_id}", response_model=schemas.TagResponse)
def get_tag_by_id(
    tag_id: int, token: str = Depends(oauth_scheme), db: Session = Depends(get_db)
):
    db_tag = service.get_tag_by_id(db, tag_id)
    if db_tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found"
        )
    return db_tag


@router.post(
    "/", response_model=schemas.TagResponse, status_code=status.HTTP_201_CREATED
)
def create_tag(
    tag: schemas.TagCreate,
    token: str = Depends(oauth_scheme),
    db: Session = Depends(get_db),
):
    return service.create_tag(db, tag)
