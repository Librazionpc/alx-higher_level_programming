#!/usr/bin/python3
a = 0
for i in range(122, 96, -1):
        a += 1
        if a % 2 == 0:
            print("{:c}".format(i - 32), end="")
        else:
            print("{:c}".format(i), end="")
