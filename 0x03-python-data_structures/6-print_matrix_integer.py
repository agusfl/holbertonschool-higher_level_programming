#!/usr/bin/python3
"""
Function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]:
                print(f"{i}", end=" ")
            else:
                print(f"{i}", end="")
        print()
