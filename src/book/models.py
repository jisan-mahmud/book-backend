from ..database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(UUID(as_uuid= True), primary_key= True, default= uuid.uuid4)
    name = Column(String(100), nullable= False)
    author = Column(String(100), nullable= False)