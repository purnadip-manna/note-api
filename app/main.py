from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from src.routers import api
from src.database import Base, engine
from src.config import API_PREFIX
from src.routers.handlers.http_error import http_error_handler


def get_application() -> FastAPI:
    # load environment variables
    load_dotenv()
    # create application
    application = FastAPI(title="Notes API", description="Simple Notes APIs")
    # include all routers
    application.include_router(api.router, prefix=API_PREFIX)
    ## Add exception handlers
    application.add_exception_handler(HTTPException, http_error_handler)
    # create database tables
    Base.metadata.create_all(bind=engine)

    return application


app = get_application()
