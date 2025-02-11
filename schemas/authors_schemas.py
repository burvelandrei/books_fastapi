from pydantic import BaseModel
from datetime import datetime


class AuthorsOut(BaseModel):
    id: int
    name: str
    alias: str | None
    country: str | None
    created_at: datetime


class AuthorsCreate(BaseModel):
    name: str
    alias: str | None
    country: str | None
