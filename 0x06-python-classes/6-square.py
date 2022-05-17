#!/usr/bin/python3
"""
Class square that defines a square.
"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square, attributes:
            - size (private attribute) --> it is the size of the square.
            - position (private attribute) --> position to start printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position.
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area: Returns the current square area"""
        return (self.__size*self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for pos in range(self.__position[1]):
                    print("")
            for pos in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
