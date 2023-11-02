#!/usr/bin/python3
from sys import argv


lent = len(argv)
if lent == 1:
    print("0 arguments.")
elif lent > 1:
    if (lent == 2):
        print("{:d} argument:".format(lent - 1))
    else:
        print("{:d} arguments:".format(lent - 1))
    for i in range(1, lent):
        print("{:d}: {}".format(i, argv[i]))
