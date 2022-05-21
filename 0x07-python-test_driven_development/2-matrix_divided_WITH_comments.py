#!/usr/bin/python3
"""
Module 2-matrix_divided, this module has a function that divides all
elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            if len(lists) != len(matrix[0]):
            """
            len matrix[0] es el largo de la primer lista de la matrix, seria 3
            en el caso del main de prueba.
            """
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for position in lists:
            if type(position) is not int and type(position) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            new_list.append(round(position/div, 2))
        new_matrix.append(new_list)
    return new_matrix
