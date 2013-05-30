#!whiskey-venv/bin/ipython -i

import os
import pymongo

MONGO_URI = os.environ.get('MONGOHQ_URL')
dbname = MONGO_URI.split('/')[-1]

db = pymongo.MongoClient(MONGO_URI)[dbname]
conf = db['config']
production = conf.find_one({'configtag': 'production'})
devel = conf.find_one({'configtag': 'devel'})
