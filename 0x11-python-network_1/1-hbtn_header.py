#!/usr/bin/python3
"""
    This script prints the value of header variable 'X-Request-Id'
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
