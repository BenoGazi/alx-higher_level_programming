#!/usr/bin/python3
"""Takes in a URL and send a request"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as _err:
        print("Error code: {}".format(_err.code))
