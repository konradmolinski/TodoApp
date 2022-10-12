.PHONY: serve_backend

install:
	pipenv install
	npm install


serve_frontend:
	npm run dev

serve_backend:
	cd backend && uvicorn todo_app.main:app --reload

migration_create:
	cd backend && alembic revision --autogenerate

migration_apply:
	cd backend && alembic upgrade head
