#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    i = 0
    results = []
    while (i < len(my_list)):
        if (my_list[i] % 2 == 0):
            results.append(1)
        else:
            results.append(0)
        i += 1
    return (results)
