install:
	pip install poetry && \
	poetry install

start:
	poetry run python telegram_bot/main.py