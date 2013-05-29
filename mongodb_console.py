#!whiskey-venv/bin/ipython -i

import os
import pymongo

MONGO_URI = os.environ.get('MONGOHQ_URL')
dbname = MONGO_URI.split('/')[-1]

db = pymongo.MongoClient(MONGO_URI)[dbname]
