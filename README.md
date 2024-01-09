# Rodrigo Delduca

## Intro

The architecture is simple (due to time constraints) and classic MVC-like in Flask. I deliberately added a caching layer, as I believe the data changes infrequently, so this could save the database in production.

PS. I like boring code.

## Improvements

### Docker improvements

1. Added multi-stage build to reduce image size.
2. Bumped Python version to 3.12.
3. Added support to hot reload even with gunicorn (see my post about it [nullonerror.org/2021/11/12/gunicorn-hot-reload-with-docker-compose](https://nullonerror.org/2021/11/12/gunicorn-hot-reload-with-docker-compose/)).

### Docker compose improvements

1. Added healthchecks for MySQL and Redis.
2. Added Redis for caching.
3. Redis data dir runs on a temporary volume.
3. MySQL data dir runs on a temporary volume.

Attention: I am not using a volume for MySQL data dir, so the data will be lost when the container is stopped. This is just for development purposes, in production, I would use a volume.

### Development experience improvements

1. Added black for auto formatting.
2. Added isort for auto imports sorting.
3. Added ruff for linting.
4. Created pyproject.toml for keep settings centralized.

PS. I am not using Poetry, I could. Personally, I prefer requirements.txt.

### Code improvements

1. Standardized code style with black.
2. Added type hints.
3. Added docstrings.

### Running locally

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements-dev.txt
```

Run auto formatting, linting, and type checking:

```bash
isort . && black . && ruff . && mypy .
```

PS. I know that typing in Python is controversial, I particularly don't have a strong opinion about it, I work on projects with 100% typing and with 0%.

### Project structure

1. Pydantic for request and response models.
2. SQLAlchemy for database ORM.
3. Redis for caching.
4. MySQL for database.
5. Flask for web framework.
6. Gunicorn for WSGI server.
7. Docker for containerization.
8. Docker compose for local development.
