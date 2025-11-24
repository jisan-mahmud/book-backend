from fastapi import APIRouter, Depends
from typing import Optional
from tortoise.queryset import QuerySet
from .models import Book
from .schemas import ReadBook_Pydantic, CreateBook
from fastapi_pagination import Page
from .paginations import CustomParams
from fastapi_pagination.ext.tortoise import paginate

router = APIRouter()


@router.get('/', response_model= Page[ReadBook_Pydantic])
async def books(name: Optional[str] = None, author: Optional[str] = None, params: CustomParams = Depends()) -> Page[int]:
    query: QuerySet[Book] = Book.all()
    if author:
        query = query.filter(author__icontains=author)
    if name:
        query = query.filter(name__icontains=name)

    # apply ordering
    query = query.order_by('-create_at')
    
    return await paginate(query, params= params)


@router.post('/', response_model=ReadBook_Pydantic)
async def add_book(book: CreateBook):
    obj = await Book.create(**book.dict())
    return await ReadBook_Pydantic.from_tortoise_orm(obj)
