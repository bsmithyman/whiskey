from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from whiskey import app, mongo, cloud, boto, cache, s3
from helper import generate_pageinfo
from models import User, Post

# ------------------------------------------------------------------------
# HTTP Errors

@app.errorhandler(404)
def page_not_found (error):
    pageinfo = {
        'title':        '404',
        'heading':      'you are lost',
    }
    return render_template('404.html', pageinfo = generate_pageinfo(pageinfo)), 404

@app.errorhandler(500)
def internal_error (error):
    pageinfo = {
        'title':        '500',
        'heading':      'computer over',
    }
    # Clean up DB, etc.
    return render_template('500.html', pageinfo = generate_pageinfo(pageinfo)), 500

# ------------------------------------------------------------------------
# Normal Views

@app.route('/')
def root ():
    return redirect(url_for('index'))

@app.route('/index')
def index ():
    pageinfo = {
        'title':        'index',
    }
    return render_template('index.html', pageinfo = generate_pageinfo(pageinfo))

@app.route('/animtest')
def animtest ():
    pageinfo = {
        'ajax':         True,
        'animheader':   True,
        'title':        'animtest',
        'heading':      'animation test',
    }
    return render_template('animtest.html', pageinfo = generate_pageinfo(pageinfo))

@app.route('/profile/<nickname>')
def profile (nickname):
    pageinfo = {
        'title':        'profile',
        'heading':      nickname,
    } 
    pageinfo = generate_pageinfo(pageinfo)
    pageinfo.update({'founduser': User().get({'nickname': nickname})})
    return render_template('profile.html', pageinfo = pageinfo)

@app.route('/users')
def users ():
    pageinfo = {
        'title':        'users',
        'heading':      'site users',
    }
    pageinfo = generate_pageinfo(pageinfo)
    pageinfo.update({'foundusers': User().get_all()})
    return render_template('users.html', pageinfo = pageinfo)

# ------------------------------------------------------------------------
# User Authentication

@app.route('/login', methods = ['GET', 'POST'])
def login ():
    pageinfo = {
        'title':        'login',
        'heading':      'login required',
    }
    return render_template('login.html', pageinfo = generate_pageinfo(pageinfo))

@app.route('/logout')
def logout ():
    # logout_user()
    return redirect(url_for('index'))

# ------------------------------------------------------------------------
# Test Suite

@app.route('/test')
#@login_required
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

@app.route('/forceerror')
def forceerror ():
    raise Exception   

@app.route('/modeltest')
#@login_required
def modeltest ():
    a = User()
    a['nickname'] =     'brendan'
    a['fullname'] =     'Brendan Smithyman'
    a['email'] =        'brendan@bitsmithy.net'
    a['ghlogin'] =      'bsmithyman'
    a['profile'] =      'This is a bio about me.'
    a.save()

    beninfo = {
        'nickname':     'ben',
        'fullname':     'Ben Postlethwaite',
        'email':        'post.ben.here@gmail.com',
        'ghlogin':      'bpostlethwaite',
        'profile':      'This is a bio about Ben.',
    }
         
    b = User(beninfo)
    b.save()

    a1 = User().get({'nickname': 'ben'})
    b1 = User().get_all({'email': a['email']})

    lines = []

    for eadict in [a1, b1[0]]:
        lines.append('{0!r}'.format(eadict))
        for key in eadict:
            lines.append('\t\'{0}\' -> {1}'.format(key, eadict[key]))
        lines.append('')

    return '\n'.join(lines)
