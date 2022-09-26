#!/usr/bin/python3

""" Defining a subclass Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry

    mthods:
        __init__: instantiates objects of the class
            Args:
                width (int): width of rectangle
                height (int): height of rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
