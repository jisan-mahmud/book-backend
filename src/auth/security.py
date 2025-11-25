from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

SECRET_KEY = '6569832e417b276748c03eccd1fb8c600f4c1cc37f914f51e276297a62e908c1'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_DAYS = 15
REFRESH_TOKEN_EXPIRE_MONTHS = 1

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
