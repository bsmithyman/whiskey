import os
from config import basedir, botocreds, cloudcreds, dbURL, memcacheconfig

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from whiskey import views, models, forms
