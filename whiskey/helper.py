from config import staticinfo

def generate_pageinfo (subpageinfo):
    pageinfo = staticinfo.copy()
    pageinfo.update(subpageinfo)

    return pageinfo
