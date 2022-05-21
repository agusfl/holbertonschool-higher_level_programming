#!/usr/bin/python3
"""
Module 2-matrix_divided, this module has a function that divides all
elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(errorMessage)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(errorMessage)
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for position in lists:
            if type(position) is not int and type(position) is not float:
                raise TypeError(errorMessage)
            new_list.append(round(position/div, 2))
        new_matrix.append(new_list)
    return new_matrix
