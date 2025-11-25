from .schemas import UserCreatePydantic
from .models import User
from .security import hash_password


class UserService:

    @staticmethod
    async def get_user_by_email(email: str) -> User | None:
        return await User.get_or_none(email= email)

    @staticmethod
    async def create_user(data: UserCreatePydantic) -> User:
        user: User = await User.create(
            email = data.email,
            hashed_password = hash_password(data.password)
        )

        if data.full_name:
            user.full_name = data.full_name
            user.save()

        return user