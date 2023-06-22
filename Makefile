init:
	echo 'initial'

lint:
	echo 'lint'
	poetry run pre-commit run all
