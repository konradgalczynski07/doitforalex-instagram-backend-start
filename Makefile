venv:
	python3 -m venv venv

install_deps:
	pip install -r requirements.txt

build:
	docker-compose up --force-recreate --build

up:
	docker-compose up

db:
	docker-compose up postgres

frontend:
	docker-compose up frontend

format:
	black instagram-backend --skip-string-normalization --exclude=migrations

# This commands might not work properly, I place it here so that you could easy look them up
activate:
	bash -c "venv/bin/activate"

environ:
	bash -c "set -o allexport; source .env; set +o allexport;"