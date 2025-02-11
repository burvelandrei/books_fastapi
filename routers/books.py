from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.books_schemas import BooksOut, BooksCreate
from db.db_operations import get_all_books, get_book_by_id, create_book, delete_book
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connect import get_session

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BooksOut])
async def get_books(db: AsyncSession = Depends(get_session)):
    return await get_all_books(db)


@router.post("/", response_model=BooksOut)
async def add_books(book: BooksCreate, db: AsyncSession = Depends(get_session)):
    return await create_book(book, db)


@router.get("/{book_id}/", response_model=BooksOut)
async def get_book(book_id: int, db: AsyncSession = Depends(get_session)):
    book = await get_book_by_id(book_id, db)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}/")
async def delete(book_id: int, db: AsyncSession = Depends(get_session)):
    book = await get_book_by_id(book_id, db)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    await delete_book(book, db)
    return JSONResponse(content={"message": "Book delete"}, status_code=204)
