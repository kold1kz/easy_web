all: build up
	docker compose build

up:
	docker compose up

down:
	docker compose down

build:
	docker compose build
