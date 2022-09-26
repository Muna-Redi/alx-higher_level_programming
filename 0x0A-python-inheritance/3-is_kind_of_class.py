#!/usr/bin/python3

"""Defining a function that checks
   an object belongs to a class or is inherited
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance\
        of a class that inherited from

    Args:
        obj (object): The object to be tested for membership to a class
        a_class (class): The class

    Return: True or false

    Raises:
        typeError
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
