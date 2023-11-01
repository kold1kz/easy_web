all: up
	
up:
	docker compose up -d

down:
	docker compose down
	
build:
	docker compose build
	
build2:
	docker build -t myapp:latest

