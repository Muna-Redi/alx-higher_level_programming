#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    size = len(my_list)

# checks index for negativity or out of range and return list
    if idx < 0 or idx >= size:
        return (my_list)

# deletes index item
    del my_list[idx]

# return list
    return (my_list)
