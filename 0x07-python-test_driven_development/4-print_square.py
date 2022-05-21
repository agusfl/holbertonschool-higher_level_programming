#!/usr/bin/python3
"""
Module 4-print_square, this module has a function that prints a square
with the character: #
"""


def print_square(size):
    """
    Function that prints a square with the character: #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
