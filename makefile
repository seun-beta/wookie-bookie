build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show_logs:
	docker compose -f local.yml logs

config:
	docker compose -f local.yml config

migrate:
	docker compose -f local.yml run --rm api python3 manage.py migrate

test:
	docker compose -f local.yml run --rm api python3 manage.py test apps/

makemigrations:
	docker compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python3 manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v


flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip env --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip env --skip migrations
