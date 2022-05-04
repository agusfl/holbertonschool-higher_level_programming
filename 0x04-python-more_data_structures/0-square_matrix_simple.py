#!/usr/bin/python3
"""
Function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    else:
        new_matrix = []
        for rows in matrix:
            new_matrix.append(list(map(lambda x: x * x, rows)))
        return new_matrix
