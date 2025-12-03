from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from tortoise.queryset import QuerySet
from fastapi_pagination.ext.tortoise import apaginate
from fastapi_pagination import Page
from .models import Book
from .schemas import ReadBook_Pydantic, CreateBook, UpdateBook
from .paginations import CustomParams
from src.auth.security import current_user
from src.auth.models import User
from .utility import IsOnwer
from fastapi_limiter.depends import RateLimiter
import logging

logger = logging.getLogger('book-router')

router = APIRouter() 


@router.get('/', response_model= Page[ReadBook_Pydantic], dependencies= [Depends(RateLimiter(times= 2, seconds= 10))] )
async def books(name: Optional[str] = None, author: Optional[str] = None, params: CustomParams = Depends()) -> Page[int]:
    query: QuerySet[Book] = Book.all()
    if author:
        query = query.filter(author__icontains=author)
    if name:
        query = query.filter(name__icontains=name)

    # apply ordering
    query = query.order_by('-created_at')

    logger.info('Test success inside docker')
    return await apaginate(query)



@router.post('/', response_model=ReadBook_Pydantic)
async def add_book(book: CreateBook, user: User = Depends(current_user)):
    obj = await Book.create(**book.model_dump(), created_by= user)
    return await obj

@router.get('/{book_id}', response_model= ReadBook_Pydantic)
async def detail_book(book_id: int):
    book: Book = await Book.get_or_none(pk= book_id)
    if not book:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'book not found')
    
    return book


@router.patch('/{book_id}')
async def update_book(book_id: int, data: UpdateBook, book: Book = Depends(IsOnwer)):
    update_book = book.update_from_dict(data.model_dump(exclude_unset= True))
    update_book.save()

    return update_book