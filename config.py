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

# MongoHQ Configuration
MONGO_URI = os.environ.get('MONGOHQ_URL')

# Redis Cloud Configuration
CACHE_TYPE = 'redis'
CACHE_REDIS_URL = os.environ.get('REDISCLOUD_URL')