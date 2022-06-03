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
# En la task 10 llamamos a super() para traer los valores de la clase Padre (Rectangle)
    
    def __str__(self):
        """
        Prints the Rectangle, we use the built in function
        __str__ - we will print with the format:
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)
# En esta parte del codigo lo que hacemos es "sobre escribir" el metodo __str__ definido
# en la clase padre (Rectangle) para que tenga el formato que nos piden aca, que es muy parecido
# simplemente que se pone al final: <size> y no: <width>/<height>.
# Es lo mismo ponerle height o width para el size ya que al ser un cuadrado tanto el height como el width
# van a medir lo mismo.
# Aca para llamar a los atributos se llama de manera publica (con el punto) y no con el doble underscore porque usamos el super().
