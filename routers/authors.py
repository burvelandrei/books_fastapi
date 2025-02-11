from fastapi import APIRouter, Depends
from schemas.authors_schemas import AuthorsOut, AuthorsCreate
from db.db_operations import get_all_authors, get_author_by_id, create_author
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_connect import get_session


router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=list[AuthorsOut])
async def get_authors(db: AsyncSession = Depends(get_session)):
    return await get_all_authors(db)


@router.post("/", response_model=AuthorsOut)
async def add_author(author: AuthorsCreate, db: AsyncSession = Depends(get_session)):
    return await create_author(author, db)


@router.get("/{author_id}/", response_model=AuthorsOut)
async def get_author(author_id: int, db: AsyncSession = Depends(get_session)):
    return await get_author_by_id(db, author_id)
