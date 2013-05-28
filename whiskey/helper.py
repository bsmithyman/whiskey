from whiskey import staticinfo
import copy

def generate_pageinfo (subpageinfo):
    pageinfo = copy.deepcopy(staticinfo)
    pageinfo.update(subpageinfo)

    return pageinfo

def add_animheader (pageinfo):
    pageinfo = copy.deepcopy(pageinfo)
    scripturl = pageinfo['media'] + 'animheader.js'
    pageinfo['scripturls'].append(scripturl)

    return pageinfo
