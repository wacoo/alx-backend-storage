#!/usr/bin/env python3
''' Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
'''
import pymongo


def list_all(mongo_collection):
    lst = mongo_collection.find()
    if lst is None:
        return []
    return lst
