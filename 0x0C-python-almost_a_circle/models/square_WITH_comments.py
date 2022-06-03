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
    
    @property
    def size(self):
        """
        Getter func for private attribute: size
        """
        return self.width # aca es lo mismo si ponemos width o height ya que van a tener el mismo valor (porque es un cuadrado).
    
    @size.setter
    def size (self, value):
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
    # Aca lo que se hace es agregar un getter (con el decorador property) y un setter (con el decorador)
    # para el atrbiuto "size".
    # Como nos dicen que el mensaje de error por si el tipo de dato que pasan no es un int y demas tiene que ser
    # el mismo que el de la clase padre, dejamos todo como esta y lo unico que hacemos es definir tanto width como
    # height iguales al valor que se pase (value) ya que como es un cuadrado van a tener el mismo "value" y en caso de
    # error nos va a traer el mensaje que se establecio en la clase padre para width y height.
 