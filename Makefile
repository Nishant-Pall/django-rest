django-run:
	docker-compose -f docker-compose.yaml up --remove-orphans

run: django-run

python-makemigrations:
	docker-compose -f docker-compose.yaml run --rm web python manage.py makemigrations
mm: python-makemigrations

python-migrate:
	docker-compose -f docker-compose.yaml run --rm web python manage.py migrate_schemas
m: python-migrate

app-build:
	docker-compose -f docker-compose.yaml build

build:app-build