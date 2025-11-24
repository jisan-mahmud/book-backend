from ..database import Base
from sqlalchemy import Column, String, Integer

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(100), nullable= False)
    author = Column(String(100), nullable= False)