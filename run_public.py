#!whiskey-venv/bin/python

settings = {
    'debug':	True,
    'host':	'0.0.0.0',
}

from whiskey import app
app.run(**settings)
