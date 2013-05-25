#!whiskey-venv/bin/python

settings = {
    'debug':	True,
    'host':	'127.0.0.1',
}

from whiskey import app
app.run(**settings)
