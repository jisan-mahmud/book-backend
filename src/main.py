from fastapi import FastAPI
from src.book.router import router as book_router
from src.auth.router import router as auth_router
from src.database import init_db, close_db
from fastapi_pagination import add_pagination


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
    await init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

print(app.servers)
