#!/bin/bash

# Пример ожидания доступности базы данных PostgreSQL
alembic revision --autogenerate -m "Migration message"

alembic upgrade head

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

