import logging
from sqlmodel import create_engine, Session
from app.core.config import settings
from app.infrastructure.models import metadata


async def connect_db():
    try:
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
        return engine
    except Exception:
        logging.exception("Could not connect to database")
        raise


async def get_session(engine):
    with Session(engine) as session:
        yield session


async def create_db_and_tables(engine):
    metadata.create_all(engine)
