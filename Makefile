install:
	- pnpm install
	- poetry install

server:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

prepare:
	poetry run pre-commit run --all-files
