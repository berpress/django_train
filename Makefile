start:
	@poetry run src/manage.py runserver

env:
	source ./env/bin/activate

migrate:
	@poetry run src/manage.py migrate

make_migrate:
	@poetry run src/manage.py makemigrations


