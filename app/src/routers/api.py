from fastapi import APIRouter

from . import movies
from . import genres
from ..config import ROUTE_PREFIX_V1

router = APIRouter()

router.include_router(movies.router, prefix=ROUTE_PREFIX_V1)
router.include_router(genres.router, prefix=ROUTE_PREFIX_V1)
