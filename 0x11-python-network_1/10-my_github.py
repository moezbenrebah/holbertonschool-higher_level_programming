#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id.
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
