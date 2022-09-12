#!/usr/bin/python

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for indx in range(0, x):
        try:
            print("{:d}".format(my_list[indx]), end='')
            count += 1
        except TypeError:
            pass
        except ValueError:
            continue
    print()
    return (count)
