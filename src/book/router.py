from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CreateBook
from ..database import get_db
from .models import Book

router = APIRouter()

@router.get('/')
def books(request: Request):
    return {'success': True}


@router.post('/')
async def add_book(request: Request, book: CreateBook, db: AsyncSession = Depends(get_db)):
    new_book = Book(**book.__dict__)
    db.add(new_book)
    await db.commit()

    return new_book
