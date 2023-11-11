#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    if a_dictionary is not None:
        key_arry = []
        for key in a_dictionary:
            key_arry.append(key)
        n = len(key_arry)
        for i in range(n):
            for j in range(0, n-i-1):
                if key_arry[j] > key_arry[j+1]:
                    key_arry[j], key_arry[j+1] = key_arry[j+1], key_arry[j]
        for key in key_arry:
            print("{}: {}".format(key, a_dictionary[key]))
