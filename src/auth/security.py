from passlib.context import CryptContext
from jose import jwt, JWTError, ExpiredSignatureError
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

async def is_authenticated(token: str = Depends(oauth2_scheme)) -> User | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user_id: uuid = uuid.UUID(payload.get('user_id'))
        user: User = await User.get_or_none(id= user_id)
        return user
    except ExpiredSignatureError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'Token has expire',
            headers= {'WWW-Authenticate': 'Bearer'}
        )
    except JWTError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'Could not valid jwt',
            headers= {'WWW-Authenticate': 'Bearer'}
        )