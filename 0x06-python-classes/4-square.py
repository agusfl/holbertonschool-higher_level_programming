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
        self.__size = size

    @property
    def size(self):
        """
        This is the Getter (accessors)
        Our our private __size variable is returned.
        The decorator: @property is used
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set value
        Argument Value: set size to 0 if value is < 0 and 1000 if
        value is > 1000 or set value to value if it is between 0 and 1000.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area: Returns the current square area"""
        return (self.__size*self.__size)
