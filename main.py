from fastapi import FastAPI

from app.core.connection import create_db_and_tables, engine
from app.routes.router import router

app = FastAPI()


app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables(engine)
