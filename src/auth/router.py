from fastapi import APIRouter, HTTPException
from .schemas import UserCreatePydantic, UserRead
from .services import UserService
router = APIRouter()


@router.post('/signup', response_model= UserRead)
async def signup(user: UserCreatePydantic):
    existing = await UserService.get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code= 400, detail= 'this user already exist')
    user = await UserService.create_user(user)
    return user