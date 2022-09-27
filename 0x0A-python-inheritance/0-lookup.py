#!/usr/bin/python3
""" defining a function that returns a list
    of all attributes and methods of an object
"""


def lookup(obj):
    """
    Returns all objects in an objects dictionary as a list
    """
    return dir(obj)
