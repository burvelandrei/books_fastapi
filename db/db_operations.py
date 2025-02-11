from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Book, Author
from schemas.books_schemas import BooksCreate
from schemas.authors_schemas import AuthorsCreate
from fastapi import HTTPException


async def get_all_books(db: AsyncSession):
    books = await db.execute(select(Book))
    return books.scalars().all()


async def get_book_by_id(id: int, db: AsyncSession):
    book = await db.execute(select(Book).where(Book.id == id))
    return book.scalar_one_or_none()


async def create_book(book_data: BooksCreate, db: AsyncSession):
    book = Book(
        title=book_data.title,
        description=book_data.description,
        date_publication=book_data.date_publication,
        author_id=book_data.author_id,
    )
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book

async def delete_book(book, db: AsyncSession):
    await db.delete(book)
    await db.commit()

async def get_all_authors(db: AsyncSession):
    authors = await db.execute(select(Author))
    return authors.scalars().all()


async def get_author_by_id(id: int, db: AsyncSession):
    author = await db.execute(select(Author).where(Author.id == id))
    return author.scalar_one_or_none()


async def create_author(author_data: AuthorsCreate, db: AsyncSession):
    author = Author(
        name=author_data.name,
        alias=author_data.alias,
        country=author_data.country,
    )
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return author


async def delete_author(author, db: AsyncSession):
    await db.delete(author)
    await db.commit()
