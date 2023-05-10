#!/usr/bin/env python3
''' In this tasks, we will implement a get_page function (prototype:
def get_page(url: str) -> str:). The core of the function is very simple.
It uses the requests module to obtain the HTML content of a particular
URL and returns it.

Start in a new file named web.py and do not reuse the code written in
exercise.py.

Inside get_page track how many times a particular URL was accessed in
the key "count:{url}" and cache the result with an expiration time of
10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response
and test your caching.

Bonus: implement this use case with decorators.
'''
import requests
import redis
from functools import wraps
from typing import Callable


db = redis.Redis()


def count_call(method: Callable) -> Callable:
    ''' count number of time a website is accessed '''
    @wraps(method)
    def function(url):
        ''' wrap function '''
        db.incr('count: {}'.format(url))
        db.expire('count: ' + url, 10)
        return method(url)
    return function


@count_call
def get_page(url: str) -> str:
    ''' fetch content from url '''
    db = redis.Redis()
    return requests.get(url).text


url = 'https://pythontic.com/database/redis/list'
print(get_page(url))
print(get_page(url))
print(get_page(url))
print(get_page(url))
print(db.get('count: ' + url))
