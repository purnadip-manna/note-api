from fastapi import APIRouter

from . import notes
from . import tags
from . import auth
from . import users
from ..internal import admin
from ..config import ROUTE_PREFIX_V1

router = APIRouter()

router.include_router(notes.router, prefix=ROUTE_PREFIX_V1)
router.include_router(tags.router, prefix=ROUTE_PREFIX_V1)
router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
router.include_router(auth.router, prefix=ROUTE_PREFIX_V1)
router.include_router(admin.router, prefix=ROUTE_PREFIX_V1)
