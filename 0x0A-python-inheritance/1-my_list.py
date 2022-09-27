#!/usr/bin/python3

""" Defining an inherited class Mylist"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self.copy
        list_copy.sort()
        print(list_copy)
