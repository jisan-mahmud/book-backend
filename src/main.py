from fastapi import FastAPI
from src.book.router import router as book_router
from src.auth.router import router as auth_router
from src.database import init_db, close_db
from fastapi_pagination import add_pagination
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from .logging_config import setup_logging


setup_logging()

app = FastAPI(
    title="FastAPI Book Backend",
    version="1.0.0"
)

# Include routers
app.include_router(book_router, prefix="/books", tags=["book"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])



# add pagination support globally
add_pagination(app)

# Startup / Shutdown events
@app.on_event("startup")
async def on_startup():
    await init_db() # db initialize

    # redis and rate limiter setup
    # Connect to Redis - typically you'd get this from environment variables
    r = redis.from_url("redis://localhost:6379", decode_responses=True)
    await FastAPILimiter.init(r)

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()