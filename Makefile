.PHONY: serve_backend

install:
	pipenv install
	npm install 


serve_frontend:
	npm run dev

serve_backend:
	uvicorn backend.todo_app.main:app --reload