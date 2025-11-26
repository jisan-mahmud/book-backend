from tortoise import Tortoise
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

async def init_db():
    """
    Initialize Tortoise ORM. Call this at startup.
    """
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules= {
                "auth": ["src.auth.models"],
                "book": ["src.book.models"],
            },
    )
    # Automatically generate database tables
    await Tortoise.generate_schemas()

# Optional: Close connections on shutdown
async def close_db():
    await Tortoise.close_connections()
