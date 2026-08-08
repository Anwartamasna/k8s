from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int | None = None


class CreateBook(BaseModel):
    title: str
    author: str
    year: int
