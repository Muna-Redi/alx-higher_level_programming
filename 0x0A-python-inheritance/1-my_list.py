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
        self.sort()
        print(self)
