install:
	poetry install

install-ci:
	poetry config virtualenvs.create false
	poetry install -vv

format:
	pycln -a yaeb tests
	isort yaeb tests
	black -S yaeb tests

lint:
	pycln -c yaeb tests
	isort -c yaeb tests
	black -S --check yaeb tests
	mypy yaeb tests
	flake8 .

test:
	pytest --cov-report term-missing --cov=yaeb
