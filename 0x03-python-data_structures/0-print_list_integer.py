#!/usr/bin/python3

def print_list_integer(my_list=[]):
    s = len(my_list)
    for i in range(s):
        print("{:d}".format(my_list[i]))
