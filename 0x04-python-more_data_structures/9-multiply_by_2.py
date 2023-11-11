#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}

    if a_dictionary is not None:
        for dkey in a_dictionary:
            new_dict[dkey] = a_dictionary[dkey] * 2
    return new_dict
