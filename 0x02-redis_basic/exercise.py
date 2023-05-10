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
from typing import Union, Callable, Optional


def count_calls(self, method: Callable) -> Callable:
    ''' count number of times this method is called '''
    @wrapper(method)
    def func(self, *args, **kwargs):
        ''' rapper function '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return func


class Cache:
    '''
    Cache class that handles caching operation
    '''
    def __init__(self) -> None:
        '''
        init Chache during instantiation
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        stores data to radis and returns id
        '''
        id1 = str(uuid.uuid4())
        self._redis.set(id1, data)
        return id1

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        ''' returns converted data or original byte '''
        result = self._redis.get(key)
        if not key or not result or not callable(fn):
            return result
        return fn(result)

    def get_str(self, key: str) -> str:
        ''' returns str version of key value '''
        val = self._redis.get(key)
        return val.decode('utf_8')

    def get_int(self, data: str) -> int:
        ''' returns int version of key value '''
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val
