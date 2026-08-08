from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import book_router
from src.db import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(book_router)
