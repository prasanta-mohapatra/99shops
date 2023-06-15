import logging

from sqlmodel import create_engine

from app.core.config import settings
from app.infrastructure.models import metadata

try:
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
except Exception:
    logging.exception("Could not connect to database")
    raise


def create_db_and_tables(db_engine):
    metadata.create_all(db_engine)
