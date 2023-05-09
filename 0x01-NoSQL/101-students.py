#!/usr/bin/env python3
''' Write a Python function that returns all students sorted by average score:

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore
'''
import pymongo


def top_students(mongo_collection):
    return(list(mongo_collection.find().sort(score)))
