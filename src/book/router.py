from fastapi import APIRouter
from typing import List, Optional
from .models import Book
from .schemas import ReadBook_Pydantic, CreateBook_Pydantic  # Use the tortoise_pydantic models

router = APIRouter()

@router.get('/', response_model=List[ReadBook_Pydantic])
async def books(name: Optional[str] = None, author: Optional[str] = None):
    query = Book.all()
    if author:
        query = query.filter(author__icontains=author)
    if name:
        query = query.filter(name__icontains=name)
    
    return await ReadBook_Pydantic.from_queryset(query)


@router.post('/', response_model=ReadBook_Pydantic)
async def add_book(book: CreateBook_Pydantic):
    obj = await Book.create(**book.dict())
    return await ReadBook_Pydantic.from_tortoise_orm(obj)
