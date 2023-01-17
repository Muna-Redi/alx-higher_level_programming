#!/usr/bin/env python3
""" Script that distributes an archive to the web server, using the function
    do_deploy, (based on the file 1-pack_web_static.py)
"""


def find_peak(list_of_integers):
    """
    Returns the peak in a list of integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
