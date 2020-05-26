start:
	@poetry run manage.py runserver

env:
	@poetry run source ./env/bin/activate

migrate:
	@poetry run src/manage.py migrate

make_migrate:
	@poetry run src/manage.py makemigrations


