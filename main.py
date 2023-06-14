from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.router import router

load_dotenv()

app = FastAPI()


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
