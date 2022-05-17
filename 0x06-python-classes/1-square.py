#!/usr/bin/python3
"""
Class square that defines a square.
"""


class Square:
    """Class Square"""
    def __init__(self, size):
        """
        Initialize the square, attributes:
            size --> it is the size of the square.
        Reason for size to bue a private attribute (__size):
        The size of a square is crucial for a square, many things depend of it
        (area computation, etc.), so you, as class builder, must control the
        type and value of this attribute. One way to have the control is to
        keep it privately. You will see in next tasks how to get, update and
        validate the size value.
        """
        self.__size = size
