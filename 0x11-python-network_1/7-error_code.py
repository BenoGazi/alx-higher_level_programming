#!/usr/bin/python3
"""Posts Data"""

if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    if res.status_code != requests.codes.ok:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
