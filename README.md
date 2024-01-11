# Rodrigo Delduca

## Question 1

### Setup

Just run the following command:

```bash
make setup
```

### Running the tests

Just run the following command:

```bash
make tests
```

Open coverage report:

```bash
open htmlcov/index.html
```

### Running locally through Docker compose

Just run the following command:

```bash
make run
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

### Notes

I tend to like boring code.

I used Pydantic (Flask Pydantic) because I think it's a great tool for validating input and output. I added a caching layer, created a generic decorator, and even used pickle to hash all the parameters, assuming the data changes infrequently, so a cache would be beneficial.

I improved the Docker file to use a multi-stage build and other improvements.

I improved the Docker Compose, added health checks for Redis and MySQL, ensuring the application only starts when both are healthy, thus avoiding crashes at startup due to lack of database connection.

I added some typing, and I know this can be controversial in the Python world; some love it, others hate it.

I created indexes on almost all fields. This could be bad as it might increase the database's disk space, but if that becomes an issue, particularly in production, partial indexes could be used.

I used Clean Architecture and Clean Code moderately. I particularly like the approach of using use cases to keep controllers lean.

Due to lack of time, I only wrote tests for the endpoints, but they cover 99-100%. Normally at work, I write tests 1:1; for every file, there's a test file covering all statements.

There are several things that could be improved, like using Flask Config for configurations.

## Question 2
