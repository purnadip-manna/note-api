###
# Properties configurations
###
import os

API_PREFIX = "/api"

ROUTE_PREFIX_V1 = "/v1"

DB_URL = os.getenv("DB_URL")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv("SECRET_KEY")
