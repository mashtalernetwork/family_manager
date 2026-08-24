.PHONY: up down test lint format migration migrate

up:
	docker compose up --build

down:
	docker compose down

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

migration:
	alembic revision --autogenerate -m "$(message)"

migrate:
	alembic upgrade head
