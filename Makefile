install:
	poetry install
dev:
	poetry run flask --app page_analyzer:app run

lint:
		poetry run flake8 page_analyzer

PORT ?= 7000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

create-db:
	createdb project-83

load:
	psql project-83 < database.sql

