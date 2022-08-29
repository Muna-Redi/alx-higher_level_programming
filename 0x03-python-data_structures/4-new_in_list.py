#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    list_size = len(my_list)
    if 0 > idx or idx >= list_size:
        return new_list
    else:
        new_list[idx] = element
        return new_list
