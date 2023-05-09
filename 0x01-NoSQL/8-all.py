#!/usr/bin/env python3
''' Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
'''
import pymongo
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection):
    ''' resturns a list of all documents in a collection '''
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
