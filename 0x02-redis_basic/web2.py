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


db = redis.Redis()


def count_page_access(method):
    ''' count number of time a website is accessed '''
    @wraps(method)
    def func(url):
        ''' wrap function '''
        ckey = 'cached:' + url
        cdata = db.get(ckey)
        if cdata:
            return cdata.decode('utf-8')

        key = 'count:' + url
        db.incr(key)
        page = method(url)
        db.set(ckey, page)
        db.expire(ckey, 10)
        return page
    return func


@count_page_access
def get_page(url: str) -> str:
    ''' fetch content from url '''
    return requests.get(url).text
