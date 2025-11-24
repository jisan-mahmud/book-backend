from fastapi import FastAPI
from src.book.router import router as book_router
from src.database import init_db, close_db

app = FastAPI(
    title="FastAPI Book Backend",
    version="1.0.0"
)

# Include routers
app.include_router(book_router, prefix="/books", tags=["book"])

# Startup / Shutdown events
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()
