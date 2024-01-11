import pickle

import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


def test_get_by_id_404_not_found(mocker, client):
    def mock_get_redis():
        class MockRedis:
            def get(self, key):
                return None

            def setex(self, key, ttl, value):
                pass

        return MockRedis()

    mocker.patch("app.cache.redis.get_redis", side_effect=mock_get_redis)

    response = client.get("/v1/404")
    assert response.status_code == 404


def test_get_by_id_200_found_not_in_cache(mocker, client):
    def mock_get_redis():
        class MockRedis:
            def get(self, key):
                return None

            def setex(self, key, ttl, value):
                pass

        return MockRedis()

    mocker.patch("app.cache.redis.get_redis", side_effect=mock_get_redis)

    client.post(
        "/v1/bulk",
        json={
            "items": [
                {
                    "title": "title",
                    "uri": "uri",
                    "date": "2021-01-01",
                }
            ]
        },
    )

    response = client.get("/v1/1")
    assert response.status_code == 200
    assert response.json == {
        "date": "Fri, 01 Jan 2021 00:00:00 GMT",
        "title": "title",
        "uri": "uri",
    }


def test_get_by_id_200_found_in_cache(mocker, client):
    def mock_get_redis():
        class MockRedis:
            def get(self, key):
                return pickle.dumps({})

        return MockRedis()

    mocker.patch("app.cache.redis.get_redis", side_effect=mock_get_redis)

    response = client.get("/v1/1")
    assert response.status_code == 200
    assert response.json == {}


def test_bulk_200(client):
    response = client.post(
        "/v1/bulk",
        json={
            "items": [
                {
                    "title": "title",
                    "uri": "uri",
                    "date": "2021-01-01",
                }
            ]
        },
    )

    assert response.status_code == 200
    assert response.json == {"ok": True}


def test_bulk_500(mocker, client):
    # Not sure why the exception is not being raised.
    mocker.patch("app.blueprints.v1.avaaz.bulk_insert", side_effect=Exception("bad"))

    response = client.post(
        "/v1/bulk",
        json={
            "items": [
                {
                    "title": "title",
                    "uri": "uri",
                    "date": "2021-01-01",
                }
            ]
        },
    )

    assert response.status_code == 500
    assert response.json == {"ok": False}


def test_fuzzy_search_404_not_found(mocker, client):
    def mock_get_redis():
        class MockRedis:
            def get(self, key):
                return None

            def setex(self, key, ttl, value):
                pass

        return MockRedis()

    mocker.patch("app.cache.redis.get_redis", side_effect=mock_get_redis)

    response = client.get("/v1/?contains=foo")
    assert response.status_code == 404


def test_fuzzy_search_200_all_filters(mocker, client):
    def mock_get_redis():
        class MockRedis:
            def get(self, key):
                return None

            def setex(self, key, ttl, value):
                pass

        return MockRedis()

    mocker.patch("app.cache.redis.get_redis", side_effect=mock_get_redis)

    client.post(
        "/v1/bulk",
        json={
            "items": [
                {
                    "title": "title",
                    "uri": "uri",
                    "date": "2021-01-01",
                }
            ]
        },
    )

    response = client.get("/v1/?contains=title&before=2021-01-02&after=2021-01-01&uri=uri")  # fmt: skip
    assert response.status_code == 200
