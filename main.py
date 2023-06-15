from fastapi import FastAPI
from app.core.connection import connect_db, create_db_and_tables
from app.routes.router import router

app = FastAPI()


app.include_router(router)


@app.on_event("startup")
async def on_startup():
    engine = await connect_db()
    await create_db_and_tables(engine)
