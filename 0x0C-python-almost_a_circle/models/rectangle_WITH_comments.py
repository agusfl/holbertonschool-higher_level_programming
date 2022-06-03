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
        for break_line in range(self.__y): # Aca printeamos la cantidad de break lines que se pase en el argumento 'y'.
            print()
        for row in range(self.__height): # Esto es para ver la cantidad de filas que necesitamos imprimir
            for blank in range(self.__x): # Esto es para ver cuantos espacios en blanco nos piden que pongamos, lo vemos en el argumento 'x'.
                print(" ", end="")
            for column in range(self.__width): # Aca vemos cuantos "#" hay que imprimir (osea cuantas columnas).
                print("#",  end="")
            print() # Ipmrimimos un salto de linea al final.

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
            # Se hace un if para chequear si "args" existe (if args) y no es None (osea no esta vacio).
            for position, arg in enumerate(args):
            # Usamos el metodo enumerate para poder hacer el "unpack".
                if position > (len(attrs) - 1): 
                # Si la posicion en la que se esta en el loop es mayor al largo
                # de la lista attrs - 1 osea: 4 quiero que haga un break ya que
                # no tenemos ningun atributo para asignar a lo que sea que 
                # pasen.
                    break
                else:
                    setattr(self, attrs[position], arg)
                    # Usamos el metodo setattr para setear el objeto que pasen (hacemos referencia a esto con "self")
                    # Como segundo argumento le pasamos lo que este en la lista "attr" en la posicion que estemos recorriendo
                    # dentro del for. 
                    # Como ultimo argumento le pasamos "arg" que es lo que vamos a asignar, esto lo sacamos de la iteracion
                    # dentro del for que itera lo que este en "args" osea los argumentos variables que se pasen dentro del metodo
                    # que estamos creando ("update").
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # Si no se entra en el primer if, osea si "args" esta vacio, entonces se viene para este else y lo que hacemos aca
        # es un for para que itere por "kwargs" y usamos el metodo items() para obtener un diccionario (key-value) de los argumentos
        # variables que se pasen cuando se llama al metodo que creamos "update", asi los podemos asignar con la funcion setattr, osea
        # asignamos cada "key" a su correspondiente "value". Ejemplo en el 8-main.py pasan en el primer "r1.update(height=1)", en este
        # caso "height" seria la key y "1" seria el value.
        # Aca no es necesario usar la lista "attrs" que habia creado para el primer if ya que la "key" que te pasan como argumento va
        # a ser el atributo correspondiente que tenes que asignar.

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of a Rectangle
        instance.
        This dictionary must contain:
        - id
        - width
        - height
        - x
        - y
        """
        return self.__dict__
# Aca usamos el metodo especial, el built in __dict__ para obtener la representacion en forma de
# diccionario de la instancia con la que se llame a "to_dictionary".
