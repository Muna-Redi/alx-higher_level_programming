#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if type(my_list) is list:
        new_list = my_list.copy()

    if len(my_list) > 0:
        for i in range(len(new_list)):
            if new_list[i] % 2 == 0:
                new_list[i] = True
            else:
                new_list[i] = False

    return (new_list)
