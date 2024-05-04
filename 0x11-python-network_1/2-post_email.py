#!/usr/bin/python3
"""Takes in a URL and an email and sends a POST request"""
if __name_ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    e_mail = sys.argv[2]
    pl = {'email': e_mail}
    pl = urllib.parse.urlencode(pl)
    pl = pl.encode('ascii')
    req = urllib.request.Request(url, pl)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
