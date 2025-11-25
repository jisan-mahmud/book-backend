from .schemas import UserCreatePydantic
from .models import User
from .security import hash_password


class UserService:

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        return await User.get_or_none(email= email)

    @staticmethod
    async def create_user(data: UserCreatePydantic) -> User:
        user_data = {
            "email": data.email,
            "hashed_password": hash_password(data.password)
        }

        if getattr(data, 'full_name', None):
            user_data['full_name'] = data.full_name

        user = await User.create(**user_data)
        return user