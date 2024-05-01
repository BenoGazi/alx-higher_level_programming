#!/usr/bin/python3
"""
Takes in a URL, send a requst to the URL and
displays the value of the X-Request-Id
variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys
"""Get the URL From the command-line"""
url = sys.argv[1]
"""Send a request to the URL"""
with urllib.request.urlopen(url) as response:
    """Get the value of the X-Request-Id header"""
    req_header = response.headers.get('X-Request-Id')
    print(req_header)
