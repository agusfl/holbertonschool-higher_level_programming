#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Create a class Square that inherits from class: Rectangle.
"""


class Square(Rectangle):
    """Class Square - is a sub class of Rectangle."""
    def __init__(self, size):
        self.__size = size # instanciamos size tal cual nos pide la letra.
        super().integer_validator("size", size)
        # Usamos la funcion creada en la clase: BaseGeometry --> integer_validator, esto lo podemos hacer ya que
        # la clase Rectangle tiene herencia de la clase BaseGeometry, entonces al decir que nuestra clase Square
        # es "hija" (hereda) de la clase Rectangle y esto nos da acceso a los atributos y metodos que hereda la
        # clase Rectangle de BaseGeometry.
        super().__init__(size, size) 
        # En esta ultima linea de codigo llamamos con la funcion super() a la clase padre (Rectangle) y con el
        # __init__ la instanciamos con los valores que se pasen como: size y size - un size seria para el width
        # y el otro size seria para el height que son las variables que estan definidas dentro de la clase Rectangle.
        # Un cuadrado siempre va a tener todos los lados iguales por eso es que solo tenemos un atributo "sizse"
        # dentro del __init__ de nuestra clase Square, ejemplo en el main se crea una instancia de la clase Square
        # llamada "s" y se le pasa como argumento size: 13, por lo tanto el area de este cuadrado va a ser:
        # 13 * 13 (size * size) --> 169.

# Se ve que en main se usa el metodo: area() y aca no lo definimos, como dije anteriormente esto se puede hacer
# gracias a que el metodo area esta definido en la clase padre de Square (osea en la clase: Rectangle).
