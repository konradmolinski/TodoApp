#!/usr/bin/env bash
set -e

## migrate database
alembic upgrade head

## Running passed command
if [[ "$1" ]]; then
	eval "$@"
else
	uvicorn todo_app.main:app --port 8000 --host 0.0.0.0 --reload
fi
