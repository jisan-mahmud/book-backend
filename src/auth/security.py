from passlib.context import CryptContext
from jose import jwt, ExpiredSignatureError
from .models import User
from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_DAYS = 15
REFRESH_TOKEN_EXPIRE_MONTHS = 1

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    try:
        return pwd_context.verify(plain, hashed)
    except:
        return False

def create_access_token(user_id: int) -> str:
    expire = datetime.now() + timedelta(days= ACCESS_TOKEN_EXPIRE_DAYS)
    return jwt.encode({'user_id': str(user_id), 'exp': expire}, SECRET_KEY, ALGORITHM)

def create_refresh_token(user_id: int) -> str:
    expire = datetime.now() + timedelta(days= REFRESH_TOKEN_EXPIRE_MONTHS)
    return jwt.encode({'user_id': str(user_id), 'exp': expire}, SECRET_KEY, ALGORITHM)

def refresh_to_access_token(refresh_token: str) -> str:
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise Exception("Invalid refresh token")
        
        user_id = uuid.UUID(user_id)
        new_access_token = create_access_token(user_id)
        return new_access_token, user_id

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


async def current_user(token: str = Depends(oauth2_scheme)) -> User | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user_id: uuid = uuid.UUID(payload.get('user_id'))
        user: User = await User.get(id= user_id)
        return user
    except ExpiredSignatureError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'Token has expire',
            headers= {'WWW-Authenticate': 'Bearer'}
        )
    except:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'Could not valid jwt',
            headers= {'WWW-Authenticate': 'Bearer'}
        )
