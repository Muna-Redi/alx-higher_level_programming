#!/usr/bin/python3
from sys import argv, exit

if __name__ == "__main__":
    lenght = len(argv) - 1
    result = 0
    if lenght == 0:
        print("{:d}".format(result))
        exit(0)
    for w in (argv):
        if w == argv[0]:
            continue
        w = int(w)
        result += w
    print("{:d}".format(result))
