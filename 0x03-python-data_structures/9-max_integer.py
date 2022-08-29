#!/usr/bin/python3

def max_integer(my_list=[]):
    # checking for an empty list
    if len(my_list) < 1:
        return (None)

    # using the sort method 
    my_list.sort()

    # returning the largest number
    return (my_list[-1])
