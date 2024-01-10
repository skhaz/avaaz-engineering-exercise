# Rodrigo Delduca

## Intro

The architecture is simple (due to time constraints) and classic MVC-like in Flask. I deliberately added a caching layer, as I believe the data changes infrequently, so this could save the database in production.

What we have?

We have 3 endpoints (described below): the first one is for bulk insert, where you can submit a JSON in the request body, and all the items will be inserted in a single database transaction. Then, we have a convenience endpoint to retrieve a single record by its assigned ID, and finally, we have the search endpoint.

All fields are indexed, and I'm not entirely sure how this service would be used, so I decided to keep it simple. If the size of the indexes on disk becomes a potential issue, we can consider adding partial indexes for commonly used queries.

We have caching in place, even though it wasn't required by the exercise. I believe that for this service, a caching layer is a valuable addition. Cache invalidation can be addressed later, possibly with a flush at the time of bulk insert or a more elaborate approach, such as per-item invalidation when modified through a possible patch endpoint.

I've tried to use a bit of clean code and clean architecture without going down the rabbit hole. I prefer concise and straightforward code.

Currently, I am writing tests, but unfortunately, I don't think I'll have enough time to complete them.

PS. I like boring code.

PS. I do not have a strong opinion on system architecture; I particularly prefer simple things. However, if you would like to see a project where I used FastAPI with Clean Code and Clean Architecture, I wrote about it on my company's blog.
Here's the link: https://fueled.com/the-cache/posts/backend/clean-architecture-with-fastapi/

## Questions and Answers

Q: Why there is a lot of `__init__.py` files?
A: Because mypy needs it to work properly.

Q: Why so many indexes?
A: I understand that everything has its tradeoff. Since these fields are likely to be constantly queried, I decided to use indexes, which, on the other hand, increase the database's disk size. In a production application, I would probably use partial indexes.

Q: Why cache?
A: I understand that these are data that are not frequently updated, so a cache always comes in handy to relieve the database. Implementing individual flushes became relatively straightforward, and of course, it could be improved, but due
to time constraints, I opted to create a hash with the parameters in a generic decorator.

Q: Why are you not using Flask Config?
A: Time constraints.

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

Run auto formatting, and linting:

```bash
isort . && black . && ruff .
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

## Usage

Run the service:

```shell
docker compose up --build
```

(Wait for everything to be ready).

Populate the database:

```shell
curl -X POST -H "Content-Type: application/json" -d @input/data.json "http://0.0.0.0:8000/v1/bulk"
```

Query it (do not forget to populate before querying):

```shell
curl "http://localhost:8000/v1/?before=2020-01-01&after=2012-01-01&contains=confort"
```

Get by ID:

```shell
curl "http://localhost:8000/v1/1"
```

## Tests

Run tests with coverage report:

```bash
PYTHONPATH=. pytest --cov-report html --cov=app
```

Open coverage report:

```bash
open htmlcov/index.html
```
