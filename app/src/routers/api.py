from fastapi import APIRouter

from . import movies
from . import genres
from . import auth
from . import users
from ..config import ROUTE_PREFIX_V1

router = APIRouter()

router.include_router(movies.router, prefix=ROUTE_PREFIX_V1)
router.include_router(genres.router, prefix=ROUTE_PREFIX_V1)
router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
router.include_router(auth.router, prefix=ROUTE_PREFIX_V1)
