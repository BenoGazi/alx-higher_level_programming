#!/usr/bin/python3
"""Sends a POST request for the body"""
if __name__ == "__main__":
    import requests
    import sys
    pl = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=pl)
    print(res.text)
