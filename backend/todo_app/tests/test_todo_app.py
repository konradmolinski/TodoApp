from collections.abc import Generator
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db() -> Generator[Any, Any, Any]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_warmup_cleanup() -> None:
    from ..crud import TodoDB

    with TodoDB(next(override_get_db()))() as db_operations:
        db_operations.clean_tasks_log()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_append_tasks_log() -> None:
    for task_type in [1, 2, 3]:
        response = client.post(
            url="/todos", data={"executor_id": 1, "task_id": task_type}
        )
        assert response.status_code == 200


def test_get_tasks() -> None:
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 0
