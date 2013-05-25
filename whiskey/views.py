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
    lines = ['<html><head><title>Test Suite</title></head><body><pre>']
    hline = '\n' + '-'*80 + '\n'

    lines.append(hline)

    lines.append('Testing S3\n')
    lines.append('Listing all buckets:')
    for bucket in s3.get_all_buckets():
        lines.append('\t{}'.format(bucket.name))

    lines.append(hline)

    testfunc = lambda x: x**2
    testval = 5

    lines.append('Testing PiCloud\n')
    
    jid = cloud.call(testfunc, testval)
    lines.append('\tRunning job: {}'.format(jid))
    result = cloud.result(jid)
    lines.append('\tResult: {0} * {0} = {1}'.format(testval, result))

    lines.append(hline)


    lines.append('</pre></body></html>')
    return '\n'.join(lines)
    
    
