from typing import Optional, Annotated
from pydantic import BaseModel, Field, AfterValidator
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Book
from .utility import must_be_letters


# Base model from Tortoise ORM (fields come from DB model)
CreateBookBase = pydantic_model_creator(
    Book,
    name="CreateBookBase",
    exclude_readonly=True
)

# Response model for reading
ReadBook_Pydantic = pydantic_model_creator(
    Book,
    name="ReadBook",
)


# Common validation for fields (DRY)
NameField = Annotated[str, Field(min_length=6)]
AuthorField = Annotated[
    str,
    Field(min_length=6),
    AfterValidator(must_be_letters)
]


class CreateBook(CreateBookBase):
    """
    Only overrides fields that need extra validation
    """
    name: NameField
    author: AuthorField


class UpdateBook(BaseModel):
    """
    Partial update with same validation rules but optional
    """
    name: Optional[NameField] = None
    author: Optional[AuthorField] = None
