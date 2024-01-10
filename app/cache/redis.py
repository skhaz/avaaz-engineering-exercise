import base64
import functools
import hashlib
import os
import pickle
from typing import Callable

from redis import ConnectionPool
from redis import Redis

_redis_pool = None

ONE_MONTH = 60 * 60 * 24 * 30  # may be more, may be less, it must have a way to flush.


def get_redis() -> Redis:  # pragma: no cover
    global _redis_pool
    if _redis_pool is None:
        _redis_pool = ConnectionPool.from_url(os.environ["CACHE_URI"])
    return Redis(connection_pool=_redis_pool)


def cache():
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            redis = get_redis()
            prefix = "cache"
            sufix = base64.b64encode(
                hashlib.sha256(
                    b"".join(
                        [
                            pickle.dumps(args),
                            pickle.dumps(kwargs),
                        ]
                    )
                ).digest()
            ).decode()

            key = ":".join([prefix, func.__module__, func.__name__, sufix])

            cached = redis.get(key)
            if cached:
                return pickle.loads(cached)  # type: ignore # I do not know why in syncronous Redis client is returning "ResponseT", a union of Awaitable and Any.

            result = func(*args, **kwargs)
            redis.setex(key, ONE_MONTH, pickle.dumps(result))
            return result

        return wrapper

    return decorator
