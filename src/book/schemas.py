from typing import Optional
from pydantic import BaseModel, field_validator, ConfigDict
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Book


CreateBookBase = pydantic_model_creator(
    Book,
    name="CreateBookBase",
    exclude_readonly=True
)

ReadBook_Pydantic = pydantic_model_creator(
    Book,
    name="ReadBook",
)


# Shared validators (base class)
class BookValidators(BaseModel):
    model_config = ConfigDict(extra="ignore")

    @field_validator("name", check_fields=False)
    def validate_name(cls, v):
        if v is not None and len(v) < 3:
            raise ValueError("Book name must be at least 3 characters long")
        return v

    @field_validator("author", check_fields=False)
    def validate_author(cls, v):
        if v is not None and not v.replace(" ", "").isalpha():
            raise ValueError("Author name must contain only letters")
        return v



class CreateBook(BookValidators, CreateBookBase):
    pass


class UpdateBook(BookValidators):
    name: Optional[str] = None
    author: Optional[str] = None
