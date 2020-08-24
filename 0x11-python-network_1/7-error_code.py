#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    try:
        res = requests.get(url)
        print(res.text)
    except requests.RequestException as e:
        print("Error code: {}".format(e))
