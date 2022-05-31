#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing the
Pascal triangle of n
"""


def pascal_triangle(n):
    """function of pascal triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(n-1):
        j = [1]
        for k in range(i):
            j.append(triangle[-1][k] + triangle[-1][k+1])
        j.append(1)
        triangle.append(j)
    return triangle
