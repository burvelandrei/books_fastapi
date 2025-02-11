from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Date
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
    date_publication = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)

    author = relationship("Author", back_populates="books")


class Author(Base, BaseMixin):
    __tablename__ = "author"

    name = Column(String(100), nullable=False)
    alias = Column(String(100), nullable=True)
    country = Column(String(100), nullable=True)

    books = relationship("Book", back_populates="author")
