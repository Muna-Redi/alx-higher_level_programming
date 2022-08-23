#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number

if temp < 0:
    temp = -(temp)

lastDigit = temp % 10
if number < 0:
    lastDigit = -(lastDigit)

if lastDigit > 5:
    string = "and is greater than 5"
elif lastDigit == 0:
    string = "and is 0"
elif lastDigit < 6:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastDigit), string)
