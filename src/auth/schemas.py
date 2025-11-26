from pydantic import BaseModel, EmailStr, model_validator, field_validator
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import User 

UserRead = pydantic_model_creator(User, include= ['id', 'username', 'email', 'full_name'])

class UserCreatePydantic(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    full_name: str | None = None

    @model_validator(mode= 'after')
    def password_validate(self):
        if self.password != self.confirm_password:
            raise ValueError('password do not match')
        
        if len(self.password) < 8:
            raise ValueError('password are too short!')
        
        return self

class LoginCredential(BaseModel):
    email: EmailStr
    password: str