from tortoise import Tortoise

DATABASE_URL = "postgres://postgres:postgres@localhost:5433/book_db" 

async def init_db():
    """
    Initialize Tortoise ORM. Call this at startup.
    """
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["src.book.models", "src.auth.models"]},
    )
    # Automatically generate database tables
    await Tortoise.generate_schemas()

# Optional: Close connections on shutdown
async def close_db():
    await Tortoise.close_connections()
