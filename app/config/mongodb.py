import os

from pymongo import MongoClient

MONGO_URL = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@mongodb:27017'
print(MONGO_URL)
conn = MongoClient(MONGO_URL)

