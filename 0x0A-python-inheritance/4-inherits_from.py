#!/usr/bin/python3

"""
Defining a function that checks if an
object is a subclass of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a class, or if the object is an\
        instance of a class that inherited from a_class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
