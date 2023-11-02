#!/usr/bin/python3
from sys import argv
lent = len(argv)
if lent == 1:
    print("0 arguments.")
elif lent > 1:
    print("{} arguments:".format(lent - 1))
    for i in range(1, lent):
        print("{}: {}".format(i, argv[i]))
