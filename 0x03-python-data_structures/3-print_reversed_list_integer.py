#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_lenght = len(my_list)
    for i in range(list_lenght):
        print("{:d}".format(my_list[list_lenght - (1 + i)]))
