from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import field_validator
from .models import Book

CreateBookBase = pydantic_model_creator(
    Book,
    name="CreateBook",
    exclude_readonly=True
)

ReadBook_Pydantic = pydantic_model_creator(
    Book,
    name="ReadBook",
)


class CreateBook(CreateBookBase):
    @field_validator("name")
    def validate_name(cls, value):
        if len(value) < 3:
            raise ValueError("Book name must be at least 3 characters long")
        return value

    @field_validator("author")
    def validate_author(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Author name must contain only letters")
        return value
