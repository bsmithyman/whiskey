from flask import render_template, flash, redirect, session, url_for, request, g
from whiskey import app, mongo, cloud, boto, cache, s3

@app.route('/')
def root ():
    return redirect(url_for('index'))

@app.route('/index')
def index ():
    return 'Hello World!'

@app.route('/test')
def testsuite ():

    testfunc = lambda x: x**2
    testvalue = 42
    testdict = {'author': 'Linus', 'title': 'Linux', 'category': 'OS'}

    jid = cloud.call(testfunc, testvalue)
    cache.set('testvalue', testvalue, timeout = 5 * 60)

    lines = ['<html><head><title>Test Suite</title></head><body><pre>']
    hline = '\n' + '-'*80 + '\n'

    lines.append(hline)

    lines.append('Testing S3\n')
    lines.append('Listing all buckets:')
    for bucket in s3.get_all_buckets():
        lines.append('\t{}'.format(bucket.name))

    lines.append(hline)

    testvalue1 = cache.get('testvalue')
    lines.append('Testing Cache\n')
    lines.append('cache.set(\'testvalue\', {0}, timeout)'.format(testvalue))
    lines.append('cache.get(\'testvalue\') --> {}'.format(testvalue1))

    lines.append(hline)

    lines.append('Testing Database\n')

    collection = mongo.db.test_collection
    id = collection.insert(testdict)

    lines.append('testdict = {!r}'.format(testdict))
    lines.append('collection.insert(testdict) --> {}'.format(id))
    lines.append('db.collection_names() --> {}'.format(mongo.db.collection_names()))
    lines.append('collection.find_one() --> {}'.format(collection.find_one()))

    lines.append(hline)

    lines.append('Testing PiCloud\n')
    
    lines.append('\tRunning job: {}'.format(jid))
    result = cloud.result(jid)
    lines.append('\tResult: {0} * {0} = {1}'.format(testvalue, result))

    lines.append(hline)


    lines.append('</pre></body></html>')
    return '\n'.join(lines)
    
    
