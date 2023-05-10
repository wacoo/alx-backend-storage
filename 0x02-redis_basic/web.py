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

import redis
import requests

db = redis.Redis()

count = 0


def get_page(url: str) -> str:
    db.set('cached:{}'.format(url), count)
    result = requests.get(url)
    db.incr('count:{}'.format(url))
    db.setex('cached:{}'.format(url), 10, db.get('cached:{}'.format(url)))
    return result.text
