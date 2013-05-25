import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Cross-Site Request Forgery protection
CSRF_ENABLED = True
SECRET_KEY = os.environ.get('CSRF_TOKEN')

# AWS / boto Configuration
botocreds = {
    'aws_access_key_id':	os.environ.get('AWS_ACCESS_KEY_ID'),
    'aws_secret_access_key':	os.environ.get('AWS_SECRET_ACCESS_KEY'),
}

# PiCloud Configuration
cloudcreds = {
    'api_key':			os.environ.get('PICLOUD_API_KEY'),
    'api_secretkey':		os.environ.get('PICLOUD_API_SECRET_KEY'),
}

# Heroku Configuration
dbURL = os.environ.get('MONGOHQ_URL')

# Memcache Configuration
memcacheconfig = {
    'servers':			os.environ.get('MEMCACHIER_SERVERS'),
    'username':			os.environ.get('MEMCACHIER_USERNAME'),
    'password':			os.environ.get('MEMCACHIER_PASSWORD'),
    'binary':			True,
}

