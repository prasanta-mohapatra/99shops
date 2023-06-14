import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


async def connect_db():
    try:
        engine = create_engine(
            f"postgresql://{settings.database_id}:{settings.database_password}@localhost/{settings.database_name}"
        )
        return engine
    except Exception:
        logging.exception("Could not connect to database")
        raise


async def create_session(engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
