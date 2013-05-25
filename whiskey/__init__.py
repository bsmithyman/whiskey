import os
from config import basedir, botocreds, cloudcreds

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.pymongo import PyMongo
from flask.ext.cache import Cache

import cloud
import boto

app = Flask(__name__)
app.config.from_object('config')

# Login Setup
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

# MongoDB Setup
mongo = PyMongo(app)

# Cache Setup
cache = Cache(app)

# PiCloud Setup
cloud.setkey(**cloudcreds)

# AWS Setup
s3 = boto.connect_s3()


from whiskey import views, models, forms
