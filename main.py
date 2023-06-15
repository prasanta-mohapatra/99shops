from fastapi import FastAPI
from app.core.connection import engine, create_db_and_tables
from app.routes.router import router

app = FastAPI()


app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables(engine)
