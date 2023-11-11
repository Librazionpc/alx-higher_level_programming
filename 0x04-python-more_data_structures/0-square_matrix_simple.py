#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    if matrix is not None:
        for i in range(0, len(matrix)):
            row = []
            for j in range(0, len(matrix[i])):
                row.append((matrix[i][j] ** 2))
            new_matrix.append(row)
    return (new_matrix)
