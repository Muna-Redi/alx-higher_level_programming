#!/usr/bin/python3
"""
    Header variable value
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info['x-request-id'])
