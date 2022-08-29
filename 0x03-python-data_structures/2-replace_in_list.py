#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_size = len(my_list)
    if 0 > idx or idx >= list_size:
        return my_list
    else:
        my_list[idx] = element
        return my_list
