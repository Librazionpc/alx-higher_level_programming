#!/usr/bin/python3
from sys import argv


lent = len(argv)
if lent == 1:
    print("0 arguments.", end="\n")
elif lent > 1:
    if (lent == 2):
        print("{} argument:".format(lent - 1), end="\n")
    else:
        print("{} arguments:".format(lent - 1), end="\n")
    for i in range(1, lent):
        print("{}: {}".format(i, argv[i]), end="\n")
