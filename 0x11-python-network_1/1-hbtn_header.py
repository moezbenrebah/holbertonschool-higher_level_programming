#!/usr/bin/python3
"""
script to takes in a URl, sends a request to it and displays the value of
X-request-Id variable found in the header of the response
"""

import urllib.request as r
from sys import argv

if __name__ == "__main__":
    req = r.Request(argv[1])
    with r.urlopen(req) as res:
        print(res.headers.get('X-Request-Id'))
