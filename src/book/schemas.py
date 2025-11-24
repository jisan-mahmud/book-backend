from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Book

# For output (reading)
ReadBook_Pydantic = pydantic_model_creator(Book, name="ReadBook")

# For input (creating)
CreateBook_Pydantic = pydantic_model_creator(Book, name="CreateBook", exclude_readonly=True)
