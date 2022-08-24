#!/usr/bin/python3
for n in range(0, 9):
    for b in range(n + 1, 10):
        if n == 8:
            print("{:d}{:d}".format(n, b))
            break
        print("{:d}{:d}".format(n, b), end=", ")
