#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        return
    for array_of_list in matrix:
        if (array_of_list == []):
            continue
        for i in array_of_list:
            print("{}".format(i), end=" ")
        print("\n")
