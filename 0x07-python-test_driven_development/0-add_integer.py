#!/usr/bin/python3

def add_integer(a, b=98):
    """"This function adds two integers

    args:
        a (int): one of number the numbers to be added
        b (int): second number optional number to be added. default value is 98

    raises:
        TypeError: a must be an integer or b must be an integer
    """
    if type(a) in [int, float]:
        if type(a) is float:
            a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) in [int, float]:
        if type(b) is float:
            b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
