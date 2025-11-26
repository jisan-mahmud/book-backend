from fastapi import FastAPI
from src.book.router import router as book_router
from src.auth.router import router as auth_router
from src.database import init_db, close_db
from fastapi_pagination import add_pagination
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from .logging_config import setup_logging
from dotenv import load_dotenv
import os

load_dotenv()


# call logging setup function (root: -> logging_config.py)
setup_logging()


async def lifespan(app: FastAPI):
    await init_db() # db initialize

    # redis and rate limiter setup
    r = redis.from_url(os.getenv('REDIS_URL'), decode_responses=True)
    await FastAPILimiter.init(r)

    yield

    await close_db() # close db connection

app = FastAPI(
    title="FastAPI Book Backend",
    version="1.0.0",
    lifespan= lifespan
)

# Include routers
app.include_router(book_router, prefix="/books", tags=["book"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])



# add pagination support globally
add_pagination(app)