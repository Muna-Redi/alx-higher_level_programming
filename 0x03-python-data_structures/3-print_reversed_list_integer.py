#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_lenght = len(my_list)
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
