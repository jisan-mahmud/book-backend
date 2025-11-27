from src.auth.security import current_user
from src.auth.models import User
from fastapi import Depends, HTTPException, status
from .models import Book

async def IsOnwer(book_id, user: User = Depends(current_user)):
    book: Book = await Book.get_or_none(id= book_id, created_by= user)
    if not book:
        raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail= 'book not found, not owned by this user'
            )
    return book