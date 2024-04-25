install:
	- npm install
	- poetry install

server:
	poetry run python manage.py runserver
