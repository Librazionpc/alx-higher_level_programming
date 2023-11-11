#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:
        new_set = []

        for i in set_1:
            for j in set_2:
                if (i == j):
                    new_set.append(j)
        return (new_set)
