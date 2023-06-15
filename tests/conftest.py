import logging
from typing import Generator
import pytest
from app.core.config import settings
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app, backend="asyncio") as c:
        yield c


@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
def prepare_database() -> Generator:
    from sqlbag.createdrop import create_database, drop_database
    from sqlalchemy import create_engine
    from app.core.connection import create_db_and_tables

    settings.TESTING = True

    logging.info(settings.SQLALCHEMY_DATABASE_URI)
    create_database(settings.SQLALCHEMY_DATABASE_URI, wipe_if_existing=True)
    logging.info("Database Created")
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    create_db_and_tables(engine)
    logging.info("Database Synced")
    yield

    logging.info("Wiping Database")
    drop_database(settings.SQLALCHEMY_DATABASE_URI)
