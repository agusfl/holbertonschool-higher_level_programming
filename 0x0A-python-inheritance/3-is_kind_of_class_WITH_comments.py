#!/usr/bin/python3
"""
Function that returns True if the object is an instance of the specified class
or if the object is an instance of a class that inherited from
otherwise return False.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to know if an object is an instance of a specified class
    or if the obj is an instance of a class that inherited from.
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False

# Este ejercicio es practicamente igual al ej anterior con la diferencia de que aca le sacamos el "type" antes de: obj
# cuando usamos la funcion: isinstance(), ya que en este caso queremos que nos diga si es una instancia siempre y
# no solo cuando es exactamente del mismo tipo de dato (misma clase).
