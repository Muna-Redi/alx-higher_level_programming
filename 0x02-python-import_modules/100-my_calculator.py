#!/usr/bin/python3
import sys
from calculator_1 import add, div, sub, mul

if __name__ != "__main__":
    exit()

lenght = len(sys.argv) - 1
result = 0

# Incomplete arguments are rejected
if lenght != 3:
    print("usage: {} <a> <operator> <b>".format(sys.argv[0]))
    exit(1)

# Get the arguments and store in variables
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

# Check the type of operation to be done and compute
if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)

# Unknown operator is rejected
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
