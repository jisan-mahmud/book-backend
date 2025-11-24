from pydantic import BaseModel, ConfigDict

class CreateBook(BaseModel):
    name: str
    author: str

    model_config = ConfigDict(from_attributes= True)


class ReadBook(BaseModel):
    id: int
    name: str
    author: str

    model_config = ConfigDict(from_attributes= True)