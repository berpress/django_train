start:
	@poetry run manage.py runserver

env:
	@poetry run source ./env/bin/activate

migrate:
	@poetry run ./manage.py migrate

make_migrate:
	@poetry run ./manage.py makemigrations


