#!/usr/bin/python3
"""
Write a class Square that defines a square.
Square instance can answer to comparators.
"""


class Square:
    """Define class Square"""
    def __init__(self, size=0):
        """Initialize"""
        self.__size = size

    @property
    def size(self):
        """Getter for: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value for: size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        "Public instance method that returns the current square area."
        return (self.size * self.size)

    def __eq__(self, other):
        """Equal operator: =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal opeator: !="""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than operator: <"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal operator: <="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than operator: >"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Greater or equal operator: >="""
        return (self.area() >= other.area())
