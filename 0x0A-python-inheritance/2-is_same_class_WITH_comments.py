#!/usr/bin/python3
"""
Function that returns True if the object is an instance of the specified class
otherwise return Fasle.
"""


def is_same_class(obj, a_class):
    """
    Function to know if an object is an instance of a specified class.
    """
    if isinstance(type(obj), a_class) is True:
        return True
    else:
        return False

# Usamos la funcion: isintance() para ver si el objeto que nos pasan como primer argumento de nuestra funcion
# "is_same_class" es una instancia de la clase que nos pasan como segundo argumento de la funcion que estamos creando
# "is_same_class". La funcion isinstance() toma como primer argumento al objeto que queres evaluar si es una instancia
# de la clase que le pasas como segundo argumento a isintance(), si el objeto que se pasa es una clase entonces se
# retorna True, de lo contrario retorna False.
# En nuestra funcion: is_same_class en la letra del ej nos piden que si es una instancia se retorne True y de lo
# contrario False, por eso lo ponemos de esta manera.
# Cuando llamamnos a la funcion: isinstance() en el primer argumento le agrego: type(obj) para que solo nos retorne
# True en el caso de que "obj" sea exactamente del mismo tipo que la clase que nos pasan, tal cual nos pide la letra.
# Hay que agregarle el type(obj) porque si pusieramos solo: isinstance(obj, a_class) entonces tmb nos daria true
# cuando se pase por ejemplo: a = 1 -> esto seria de tipo int y si ponemos: is_same_class(a, object) nos va a dar
# True ya que todas las clases heredan de "object" pero nosotros solo queremos que nos de True si ponemos el mismo
# tipo de dato, en este caso seria: is_same_class(a, int) ya que 'a' es un int.
