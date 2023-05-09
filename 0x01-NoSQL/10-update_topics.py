#!/usr/bin/env python3
''' Write a Python function that changes all topics of
a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of
topics approached in the school
'''
import pymongo


def update_topics(mongo_collection, name, topics):
    ''' update and add topics based on given name '''
    query = {'name': name}
    new_val = {'$set': {'topics': topics}}
    mongo_collection.update_many(query, new_val)
