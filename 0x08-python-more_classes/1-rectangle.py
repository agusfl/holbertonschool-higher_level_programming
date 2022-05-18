#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Getter func for private variable: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set value for: height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter func for private variable: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set value for: width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
