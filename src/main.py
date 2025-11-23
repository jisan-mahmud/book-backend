from fastapi import FastAPI
from book.router import router as book_router

app = FastAPI(
    title= 'FastAPI book backend',
    version= '1.0.0'
)


app.include_router(book_router, prefix='/book', tags=['book'])

