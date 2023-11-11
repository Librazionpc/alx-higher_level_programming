#!/usr/bin/python5

def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None and key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
