from pydantic import BaseModel
from datetime import datetime
from .authors_schemas import AuthorsOut


class BooksOut(BaseModel):
    id: int
    title: str
    description: str | None
    date_publication: datetime | None
    created_at: datetime


class BooksCreate(BaseModel):
    title: str
    description: str | None
    date_publication: datetime | None
    author_id: int
