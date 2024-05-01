#!/usr/bin/python3
"""Takes in a URL and displays the value of X"""
if __name__ == "__main__":
    import urllib.request
    import sys
    _req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(_req) as response:
        req_header = dict(response.headers).get('X-Request-Id')
        print(req_header)
