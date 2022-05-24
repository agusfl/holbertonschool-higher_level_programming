#!/usr/bin/python3
"""
Module that has a function to multiplicate 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiples two matrices
    -m_a and m_b: are matrices of type list that contains lists of type
    integers or floats.
    """

    if type(m_a) is not list or type(m_a[0]) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list or type(m_b[0]) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a[0]) == 0 or len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b[0]) == 0 or len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("m_b should contain only integers or floats")

    # For matrix mul:the number of columns in the first matrix must be equal to
    # the number of rows in the second matrix.
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    line = []
    new_matrix = []
    result = 0
    for row_ma in range(len(m_a)):
        line = []
        for col_mb in range(len(m_b[0])):
            for i in range(len(m_a[0])):
                result += m_a[row_ma][i] * m_b[i][col_mb]
            line.append(result)
            result = 0
        new_matrix.append(line)

    return new_matrix
