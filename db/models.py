from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class BaseMixin:
    """Миксин для добавления ID и created_at во все модели"""
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Book(Base, BaseMixin):
    __tablename__ = "book"

    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)

    author = relationship("Author", back_populates="books")


class Author(Base, BaseMixin):
    __tablename__ = "author"

    name = Column(String(100), nullable=False)

    books = relationship("Book", back_populates="author")
