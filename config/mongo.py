import os
from pymongo.mongo_client import MongoClient

mongodb_uri = os.environ.get('MONGO_DB_URI')
client = MongoClient(mongodb_uri)
db = client["Video"]
