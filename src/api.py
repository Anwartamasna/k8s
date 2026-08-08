from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from src.db import get_session
from src.schemas import Book, CreateBook

book_router = APIRouter(prefix="/api/v1/book")


@book_router.post("/create", response_model=Book)
def create(book: CreateBook, session=Depends(get_session)):
    db_book = Book(**book.model_dump())

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


@book_router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, session=Depends(get_session)):
    book: Book | None = session.get(Book, book_id)

    if not book:
        raise HTTPException(404, "Book not found")

    return book


@book_router.get("/books", response_model=list[Book])
def get_books(session=Depends(get_session)):
    return session.exec(select(Book)).all()
