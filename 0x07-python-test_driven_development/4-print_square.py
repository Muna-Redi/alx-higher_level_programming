#!/usr/bin/python3

""" Defines a functions that prints a square """


def print_square(size):
    """This function prints a square with the charracter '#'

    args:
        size (int): size of the square to be printed

    return:
        returns nothing

    raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) is not int:

        if (type(size) is float) and (size < 0):
            raise TypeError("size must be an integer")

        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):

        for j in range(size):
            print("#", end="")

        print()
