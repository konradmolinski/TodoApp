.PHONY: serve_backend

install:
	pipenv install
	npm install


serve_frontend:
	cd frontend && npm run dev

serve_backend:
	cd backend && uvicorn todo_app.main:app --reload

migration_create:
	cd backend && alembic revision --autogenerate

migration_apply:
	cd backend && alembic upgrade head


seed_data:
	cd backend && rm todo_app.db
	cd backend && alembic upgrade head
	cd backend && python sqlalchemy_playground.py
