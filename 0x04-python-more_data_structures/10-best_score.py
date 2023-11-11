#!/usr/bin/python3

def best_score(a_dictionary):
    name = None
    if a_dictionary is not None:
        n = 0
        for dkey in a_dictionary:
            if (a_dictionary[dkey] > n):
                n = a_dictionary[dkey]
                name = dkey
    return (name)
