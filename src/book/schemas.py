from typing import Optional, Annotated
from pydantic import BaseModel, Field, AfterValidator
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Book
from .utility import must_be_letters

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


class CreateBook(BaseModel):
    name: NameField
    author: AuthorField


class UpdateBook(BaseModel):
    name: Optional[NameField] = None
    author: Optional[AuthorField] = None
