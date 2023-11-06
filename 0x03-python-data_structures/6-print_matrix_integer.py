#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for array_of_list in matrix:
            if array_of_list is not None:
                for i in array_of_list:
                    print("{:d}".format(i), end='')
                print("")
