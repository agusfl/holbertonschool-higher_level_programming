#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry 
# Primero importamos la clase BaseGeometry que creamos en el archivo del ej anterior.
"""
Create a class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

# En este ej creamos la clase "Rectangle" que es una sub clase de "BaseGeometry", inicializamos las variables
# privadas que nos piden en la letra: width y height (variables privadas eran las que tenian dos underscores: __ )
# Con la funcion: super() llamamos al metodo: integer_validator de la clase padre: BaseGeometry y le pasamos como
# argumentos primero un string --> "width" y segundo el value que en este caso va a ser lo que pasen en: 'width'
# Esto mismo se puede hacer sin usar super() usando self --> self.integeter_validator("width", width)
