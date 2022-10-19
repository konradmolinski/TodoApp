from collections.abc import Generator
from .database import SessionLocal
from typing import Any


def get_db() -> Generator[Any, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db = next(get_db())
