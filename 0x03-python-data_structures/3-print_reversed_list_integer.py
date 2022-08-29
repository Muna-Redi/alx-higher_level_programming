#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_lenght = len(my_list)
    n = -1
    for i in range(list_lenght):
        print("{:d}".format(my_list[n]))
        n -= 1
