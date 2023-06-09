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
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' count number of times this method is called '''
    @wraps(method)
    def func(self, *args, **kwargs):
        ''' wrapper function '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return func


def call_history(method: Callable) -> Callable:
    ''' store inputs and outputs of store to radis '''
    @wraps(method)
    def func2(self, *args, **kwargs):
        ''' wrapper function '''
        ikey = method.__qualname__ + ':inputs'
        okey = method.__qualname__ + ':outputs'
        result = str(method(self, *args, **kwargs))
        self._redis.rpush(ikey, str(args))
        self._redis.rpush(okey, result)
        return result
    return func2


def replay(method: Callable) -> None:
    ''' replays the history of a function '''
    db = redis.Redis()
    name = method.__qualname__
    count = db.get(name).decode('utf-8')
    print('{} was called {} times:'.format(name, count))
    inputs = db.lrange(name + ':inputs', 0, -1)
    outputs = db.lrange(name + ':outputs', 0, -1)
    for i, o in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(name, i.decode('utf-8'),
              o.decode('utf-8')))


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

    @count_calls
    @call_history
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
