from whiskey import staticinfo

def generate_pageinfo (subpageinfo):
    pageinfo = staticinfo.copy()
    pageinfo.update(subpageinfo)

    return pageinfo

def add_animheader (pageinfo):
    pageinfo = pageinfo.copy()
    pageinfo['scripturls'].append(pageinfo['media'] + 'animheader.js')

    return pageinfo
