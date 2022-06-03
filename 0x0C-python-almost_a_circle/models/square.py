#!/usr/bin/python3
"""
Module for creating a class: Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition, inherits from Rectangle that inherits from Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize, use of super method to get values from parent class
        (Rectangle)
        """
        super().__init__(size, size, x, y, id)
