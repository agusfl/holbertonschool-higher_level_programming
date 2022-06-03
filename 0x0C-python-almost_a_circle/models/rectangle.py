#!/usr/bin/python3
"""
Create a class Rectangle that inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter func for private attribute: width
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

    @property
    def height(self):
        """
        Getter func for private attribute: height
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
    def x(self):
        """
        Getter func for private attribute: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set value for: x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter func for private attribute: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set value for: y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance
        with the character: #
        """
        for break_line in range(self.__y):
            print()
        for row in range(self.__height):
            for blank in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#",  end="")
            print()

    def __str__(self):
        """
        Prints the Rectangle, we use the built in function
        __str__ - we will print with the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        attrs = ["id", "width", "height", "x", "y"]

        if args and args is not None:
            for position, arg in enumerate(args):
                if position > (len(attrs) - 1):
                    break
                else:
                    setattr(self, attrs[position], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
