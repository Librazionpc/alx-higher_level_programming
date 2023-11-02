#!/usr/bin/python3
from sys import argv


lent = len(argv)
if lent == 1 or lent == 2:
    statements = "argument."
else:
    statements = "arguments:"
print("{:d} {}".format(lent - 1, statements))

for i in range(1, lent):
    print("{:d}: {}".format(i, argv[i]))
