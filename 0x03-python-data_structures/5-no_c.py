#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    new_string = my_string
    i = 0
    while (i < str_len):
        if new_string[i] == "c" or new_string[i] == "C":
            new_string = new_string[:i] + new_string[i + 1:]
            str_len = len(new_string)
            i = 0
            continue
        i += 1
    return new_string
