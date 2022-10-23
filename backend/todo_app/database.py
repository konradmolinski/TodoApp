from collections.abc import Generator
from typing import Any

from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import logger
from os import environ

DATABASE_URL = environ.get("DATABASE_URL", default="sqlite:///./todo_app.db")
logger.info(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def _fk_pragma_on_connect(dbapi_con: Any, con_record: Any) -> None:
    dbapi_con.execute("pragma foreign_keys=ON")


event.listen(engine, "connect", _fk_pragma_on_connect)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: Any = declarative_base()


def get_db() -> Generator[Any, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
