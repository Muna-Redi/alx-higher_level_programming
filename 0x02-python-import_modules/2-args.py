#!/usr/bin/python3
from sys import argv, exit

if __name__ == "__main__":
    lenght = len(argv) - 1
    str1 = "argument"
    count = 1
    if lenght == 1:
        str1 += ":"
    elif lenght >= 1:
        str1 += "s:"
    elif lenght == 0:
        str1 += "s."
        print("{:d} {}".format(lenght, str1))
        exit(0)
    print("{:d} {}".format(lenght, str1))
    for w in (argv):
        if w == argv[0]:
            continue
        print("{:d}: {}".format(count, w))
        count += 1
