from fastapi import APIRouter, Depends
from typing import Optional
from tortoise.queryset import QuerySet
from fastapi_pagination.ext.tortoise import apaginate
from fastapi_pagination import Page
from .models import Book
from .schemas import ReadBook_Pydantic, CreateBook
from .paginations import CustomParams
from src.auth.security import is_authenticated
from src.auth.models import User
from fastapi_limiter.depends import RateLimiter

router = APIRouter()


@router.get('/', response_model= Page[ReadBook_Pydantic], dependencies= [Depends(RateLimiter(times= 2, seconds= 10))] )
async def books(name: Optional[str] = None, author: Optional[str] = None, params: CustomParams = Depends()) -> Page[int]:
    query: QuerySet[Book] = Book.all()
    if author:
        query = query.filter(author__icontains=author)
    if name:
        query = query.filter(name__icontains=name)

    # apply ordering
    query = query.order_by('-create_at')
    
    return await apaginate(query, params= params)


@router.post('/', response_model=ReadBook_Pydantic)
async def add_book(book: CreateBook, user: User = Depends(is_authenticated)):
    obj = await Book.create(**book.dict())
    return await ReadBook_Pydantic.from_tortoise_orm(obj)
