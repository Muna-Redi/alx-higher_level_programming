#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_tup1 = len(tuple_a)
    len_tup2 = len(tuple_b)
# tuple_a and tuple_b have enough elements/params
    if len_tup1 >= 2 and len_tup2 >= 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]

# only tuple_a has enought elements/params
    elif len_tup1 >= 2 and len_tup2 <= 1:
        if len_tup2 < 1:
            a = tuple_a[0]
        else:
            a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1]

# only tuple_b has enough elements/params
    elif len_tup2 >= 2 and len_tup1 <= 1:
        if len_tup1 < 1:
            a = tuple_b[0]
        else:
            a = tuple_a[0] + tuple_b[0]
        b = tuple_b[1]

# neighter tuple_a or b has enough elements/params
    elif len_tup1 <= 1 and len_tup2 <= 1:
        if len_tup1 == 1:
            if len_tup2 == 1:
                a = tuple_a[0] + tuple_b[0]
            elif len_tup2 < 1:
                a = tuple_a[0]
        elif len_tup1 < 1:
            if len_tup2 == 1:
                a = tuple_b[0]
            else:
                a = 0
        b = 0

# returning the new tuple
    new_tuple = (a, b)
    return (new_tuple)
