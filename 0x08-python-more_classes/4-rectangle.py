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

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Prints the Recatngle
        Usamos el atributo especial __str__ para imprimir
        el rectangulo cuando se llama a la funcion print en el main con
        la clase que creamos "Rectangle" y se le pasa los dos argumentos:
        width y height.
        Guardamos lo que se va a ir printiando en la variable "string".
        Con: string[:-1] se saca el salto de linea.
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for height in range(self.__height):
            for width in range(self.__width):
                string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle.
        Info para este ej:
        https://www.codecademy.com/forum_questions/5157083753fce0354800203f
        """
        return f"Rectangle({self.width:d}, {self.height:d})"
