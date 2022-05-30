#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Create a class Square that inherits from class: Rectangle.
Este ej es muy parecido al anterior, simplemente que tenemos que sobreescribir
el metodo __str__ definido en la clase padre "Rectangle" para que ahora
en lugar de imprimir con este formato: [Rectangle] <width>/<height>
Imprima con este formato: [Square] <width>/<height>
"""


class Square(Rectangle):
    """Class Square - is a sub class of Rectangle."""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Overwrite the __str__ method of the parent class Rectangle."""
        return f"[Square] {self.__size}/{self.__size}"
