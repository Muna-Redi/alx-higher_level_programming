#!/usr/bin/python3

""" Defining a class Base

    attributes:
        __nd_objects (int): a private class attribute

    methods:
        __init__ (function): class decorator
"""


class Base:
    """  Class Base

        Attributes:
            nb_objects (int): a private class attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class decorator

        Attributes:
            id (int): integer input for id
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
