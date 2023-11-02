#!/usr/bin/python3
from sys import argv
sums = 0
lent = len(argv)
for i in range(1, lent):
    sums += int(argv[i])
print(sums)
