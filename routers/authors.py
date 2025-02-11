from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.authors_schemas import AuthorsOut, AuthorsCreate
from db.db_operations import get_all_authors, get_author_by_id, create_author, delete_author
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
    author = await get_author_by_id(author_id, db)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.delete("/{author_id}/")
async def delete(author_id: int, db: AsyncSession = Depends(get_session)):
    author = await get_author_by_id(author_id, db)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    await delete_author(author, db)
    return JSONResponse(content = {"message": "Author delete"}, status_code=204)
