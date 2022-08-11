format:
	pycln yaeb tests
	isort yaeb tests
	black -S yaeb tests

lint:
	pycln -c yaeb tests
	isort -c yaeb tests
	black -S --check yaeb tests
	mypy --strict yaeb tests

test:
	pytest --cov-report term-missing --cov
