init:
	echo 'initial'

lint:
	echo 'lint'
	poetry run pre-commit run -a

run:
	echo 'run'
	poetry run python manage.py runserver 0.0.0.0:8000

makemigrations:
	echo 'makemigrations'
	poetry run python manage.py makemigrations

migrate:
	echo 'migrate'
	poetry run python manage.py migrate
