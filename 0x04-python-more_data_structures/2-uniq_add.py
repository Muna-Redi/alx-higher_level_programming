#!/usr/bin/python3

def uniq_add(my_list):
    track = set(my_list)
    sum = 0
    for num in track:
        sum += num
    return sum
