#!/bin/usr/python3
"""
Class square that defines a square.
"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """
        Initialize the square, attributes:
            size (private attribute) --> it is the size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area: Returns the current square area"""
        return (self.__size*self.__size)
