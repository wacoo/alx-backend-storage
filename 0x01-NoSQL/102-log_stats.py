#!/usr/bin/env python3
''' Improve 12-log_stats.py by adding the top 10 of the most present
IPs in the collection nginx of the database logs:

The IPs top must be sorted (like the example below)
'''
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db1 = client['logs']
collection = db1['nginx']

print("{} logs".format(len(list(collection.find()))))
print("Methods:")
print("    method GET: {}".format(len(list(
      collection.find({method: "GET"})))))
print("    method POST: {}".format(len(list(
      collection.find({method: "POST"})))))
print("    method PUT: {}".format(len(list(
      collection.find({method: "PUT"})))))
print("    method PATCH: {}".format(len(list(
      collection.find({method: "PATCH"})))))
print("    method DELETE: {}".format(len(list(
      collection.find({method: "DELETE"})))))
status = mongo_collection.count_documents(
     {"path": "/status"})
print("{} status check".format(status))

print("IPs:")
ip_dict = [
    {
        "$group":
        {
            "_id": "$ip",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 10
    },
    {
        "$project":
        {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }
    }
]

for ip in ip_dict:
    count = ip.get('count')
    address = ip.get('ip')
    print('    {}: {}'.format(address, count))
