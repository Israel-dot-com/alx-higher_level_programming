#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{a} + {b} = {2:d}".format(a, b, add(a, b)))
    print("{a} - {b} = {2:d}".format(a, b, sub(a, b)))
    print("{a} * {b} = {2:d}".format(a, b, mul(a, b)))
    print("{a} / {b} = {2:d}".format(a, b, div(a, b)))
