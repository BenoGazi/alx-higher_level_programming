#!/usr/bin/python3
"""Displays value of the variable X-request-Id"""

if __name__ == "__main__":
    import requests
    import sys
    response = requests.get(sys.argv[1])
    meta = response.headers
    print(meta.get('X-Request-Id'))
