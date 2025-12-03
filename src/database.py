import os
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Example:
# postgres://postgres:postgres@localhost:5432/book_db

TORTOISE_CONFIG = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "models": { 
            "models": [
                "src.auth.models",
                "src.book.models",
                "aerich.models", 
            ],
            "default_connection": "default",
        }
    },
}


async def init_db():
    """
    Initialize Tortoise ORM at startup.
    """
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()


async def close_db():
    """
    Close DB connections on shutdown.
    """
    await Tortoise.close_connections()
