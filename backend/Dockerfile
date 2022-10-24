FROM python:3.10-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc postgresql-server-dev-all python-dev

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system

WORKDIR /app

# COPY . .


ENTRYPOINT [ "/app/entrypoint.sh" ]
