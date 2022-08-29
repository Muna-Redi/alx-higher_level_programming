#!/usr/in/python3

def delete_at(my_list=[], idx=0):
    size = len(my_list)

    # checks if idx is out of range or negative and return list
    if idx < 0 or idx >= size:
        return (my_list)

    # deleting the item of index idx
    else:
        del my_list[idx]

    # return modified list
    return (my_list)
