#!/usr/bin/python3


def print_last_digit(number):
    temp = number
    if (number < 0):
    	temp = -(number)
    last_digit = (number) % 10
    if (number < 0):
        last_digit = -(last_digit)
    print("{:d}".format(last_digit), end='')
    return last_digit
