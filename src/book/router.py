from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import CreateBook, ReadBook
from ..database import get_db
from .models import Book
from typing import List

router = APIRouter()

@router.get('/', response_model= List[ReadBook])
async def books(name: str= None, author: str= None, db: AsyncSession = Depends(get_db)):
    filters = []
    if author:
        filters.append(Book.author.ilike(f"%{author}%"))
    if name:
        filters.append(Book.name.ilike(f"%{name}%"))

    query = select(Book).where(*filters)
    result = await db.execute(query)
    return result.scalars().all()


@router.post('/')
async def add_book(book: CreateBook, db: AsyncSession = Depends(get_db)):
    new_book = Book(**book.__dict__)
    db.add(new_book)
    await db.commit()


    return new_book
