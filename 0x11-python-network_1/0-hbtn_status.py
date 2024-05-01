#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    data = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(data) as response:
        print ("Body response:")
        print ("\t- type: {}".format(type(response.read())))
        response.seek(0)
        print("\t- content: {}".format(response.read()))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
