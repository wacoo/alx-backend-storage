#!/usr/bin/env python3
''' Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
'''
import pymongo
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List:
    ''' resturns a list of all documents in a collection '''
    lst = mongo_collection.find()
    if not lst:
        return []
    return lst
