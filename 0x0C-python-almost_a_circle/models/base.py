#!/usr/bin/python3

""" Defining a class Base

    attributes:
        __nd_objects (int): a private class attribute

    methods:
        __init__ (function): class decorator
"""


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 
            this method returns a json string

            Args:
                list_dictionarie (list): list of dictionaries to be
                represented in json string

            returns a json string
        """

        if list_dictionaries is not None and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)

        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
            saves a list of objects to a json file

            Args:
                cls (class): class to which objects belong

                list_objs (list): list of objects of the class cls

        """

        if list_objs is not None and len(list_objs) != 0:
            file_name = cls.__name__ + ".json"
            list_dictionaries = []

            for obj in list_objs:
                list_dictionaries.append(cls.to_dictionary(obj))

            with open(file_name, 'w', encoding='utf-8') as f:
                jstring = cls.to_json_string(list_dictionaries)
                f.write(jstring)

        else:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write("")
    @staticmethod
    def from_json_string(json_string):

        new_list = []
        if json_string is None or not json_string:
            return new_list
        new_list = json.loads(json_string)
        return new_list
