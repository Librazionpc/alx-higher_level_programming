#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    lent = len(argv)
    if lent != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if (op == "+"):
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif (op == "-"):
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif (op == "*"):
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif (op == "/"):
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
