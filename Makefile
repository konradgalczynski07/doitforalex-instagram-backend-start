venv:
	python3 -m venv venv

format:
	black instagram-backend --skip-string-normalization

build:
	@docker-compose up --force-recreate --build

up:
	@docker-compose up

db:
	@docker-compose up -d postgres