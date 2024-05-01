#!/usr/bin/python3
"""Takes in a URL and displays the value of X"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        req_header = response.headers.get('X-Request-Id')
        print(req_header)
