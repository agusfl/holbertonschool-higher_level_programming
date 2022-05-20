#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    # Se incializa aca y no en el init porque es un atributo de toda la clase
    print_symbol = "#"
    # En la letra se nos indica que se tiene que incializar con este valor.

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        """
        Aca lo llamamos con Rectangle. en lugar de self porque
        number_of_instances es un atributo para toda la clase.
        Aca sumamos uno cada vez que se cree una instancia de
        cuando se incia un objeto nuevo de tipo Rectangle.
        """

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
                string += str(self.print_symbol)
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle.
        Info para este ej:
        https://www.codecademy.com/forum_questions/5157083753fce0354800203f
        """
        return f"Rectangle({self.width:d}, {self.height:d})"

    def __del__(self):
        """
        Use of del method to delete an isntance of a class and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that returns a new Rectangle instance with:
        width == height == size
        """
        return cls(width=size, height=size)
