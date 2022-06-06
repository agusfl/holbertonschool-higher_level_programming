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

    def __str__(self):
        """
        Prints the Rectangle, we use the built in function
        __str__ - we will print with the format:
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)

    @property
    def size(self):
        """
        Getter func for private attribute: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set value for: size
        The setter should assign (in this order) the width and the height
        with the same value.
        The setter should have the same value validation as the Rectangle for
        width and height - No need to change the exception error message (It
        should be the one from width).
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attrs = ["id", "size", "x", "y"]

        if args and args is not None:
            for position, arg in enumerate(args):
                if position > (len(attrs) - 1):
                    break
                else:
                    setattr(self, attrs[position], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of a Square
        instance.
        This dictionary must contain:
        - id
        - width
        - height
        - x
        - y
        """
        new_dict = {}
        attrs = ["id", "x", "size", "y"]

        for attribute in attrs:
            new_dict[attribute] = getattr(self, attribute)
        return new_dict
