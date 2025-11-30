from fastapi import APIRouter, HTTPException, Depends, Body
from .schemas import UserCreatePydantic, UserRead, LoginCredential, Refresh_token_schema
from .services import UserService
from .security import create_access_token, create_refresh_token, refresh_to_access_token, current_user
from .models import User
import uuid


router = APIRouter()


@router.post('/signup', response_model= UserRead)
async def signup(user: UserCreatePydantic):
    existing = await UserService.get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code= 400, detail= 'this user already exist')
    user = await UserService.create_user(user)
    return user

@router.post('/login')
async def login(credential: LoginCredential):
    user = await UserService.authenticate_user(credential.email, credential.password)
    if not user:
        raise HTTPException(status_code= 404, detail= {
            'error': 'Authentication fail',
            'message': 'credential are invalid'
        })
    
    access_token: str = create_access_token(user.id)
    refresh_token: str = create_refresh_token(user.id)
    response: dict = {
        'user_id': user.id,
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return response

@router.post('/access-token')
def refresh_token(refresh_token: str = Body(..., embed= True)):
    access_token, user_id = refresh_to_access_token(refresh_token)
    refresh_token = create_refresh_token(user_id)

    
    return {
        "user_id": user_id,
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@router.post('/me', response_model= UserRead)
async def current_user(user: User = Depends(current_user)):
    return user