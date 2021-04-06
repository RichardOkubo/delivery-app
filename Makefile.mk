clean:
	del /s /q *.pyc 1>nul
	del /s __pycache__
	del /q delivery.egg-info
	rmdir delivery.egg-info
	del /q .pytest_cache
	del .coverage
	del /q htmlcov
	rmdir htmlcov

no-cache:
	pip install -e .['dev'] --upgrade --no-cache

install:
	pip install -e .['dev']

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	FLASK_ENV=test
	pytest tests/ -v --cov=delivery
