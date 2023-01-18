#!/usr/bin/python3
"""
    urllib.error
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err_or:
        print('Error code: {}'.format(err_or.code))
