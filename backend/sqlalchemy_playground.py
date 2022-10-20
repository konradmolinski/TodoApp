from collections.abc import Generator
from todo_app.database import SessionLocal
from typing import Any
from todo_app.db_models import DBCategory, DBUser


def get_db() -> Generator[Any, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


session = next(get_db())


def create_seed_data() -> None:
    # users
    wojtek = DBUser(name="Wojtek", status="ACTIVATED", secret="bardzotrudnehaslo")
    konrad = DBUser(name="Konrad", status="ACTIVATED", secret="kondziowehaslo")
    # categories
    categories = [
        "Koty",
        "Łazienka",
        "Kuchnia",
        "Korytarz",
        "Salon",
        "Balkon",
        "Wojtka",
        "Konrada",
    ]
    for category in categories:
        session.add(DBCategory(title=category))
    session.add(wojtek)
    session.add(konrad)
    session.commit()


if __name__ == "__main__":
    create_seed_data()
