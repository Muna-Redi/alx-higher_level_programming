#!/usr/bin/python3

def element_at(my_list, idx):
    list_lenght = len(my_list)
    if 0 > idx or idx >= list_lenght:
        return None
    else:
        return my_list[idx]
