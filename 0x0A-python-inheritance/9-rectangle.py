#!/usr/bin/python3
"""
Create a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Method that initializes values"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of a rectangle, that is: width multiplied height
        """
        return self.__width * self.__height

    def __str__(self):
        """Prints the Rectangle with the format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
