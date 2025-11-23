from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:jisanm@localhost:5433/jisan_db"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for model
Base = declarative_base()

# Dependency for FastAPI
async def get_db():
    async with async_session() as session:
        yield session