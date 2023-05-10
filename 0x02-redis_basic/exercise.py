#!/usr/bin/env python3
''' Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes,
int or float'''
import redis
import uuid
from typing import Union


class Cache:
    ''' Cache class that handles caching operation '''
    def __init__(self) -> None:
        ''' init Chache during instantiation '''
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' stores data to radis and returns id '''
        id1 = str(uuid.uuid4())
        self._redis.set(id1, data)
        return id1
