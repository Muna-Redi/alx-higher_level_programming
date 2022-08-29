#!/usr/bin/python3

def max_integer(my_list=[]):
    # checking for an empty list
    if len(my_list) < 1:
        return ("None")

    # innitialise largest to 0
    largest = 0

    # travarse throught the list in search of the maximu number
    for num in my_list:
        if largest < num:
            largest = num

    # returning the largest number
    return (largest)
