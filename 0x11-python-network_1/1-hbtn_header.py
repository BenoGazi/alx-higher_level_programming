#!/usr/bin/python3
"""Takes in a URL and displays the value of X"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        req_header = response.headers.get('X-Request-Id')
        print(req_header)
