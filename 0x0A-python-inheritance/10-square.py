#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Create a class Square that inherits from class: Rectangle.
"""


class Square(Rectangle):
    """Class Square - is a sub class of Rectangle."""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
