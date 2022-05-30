#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class, otherwise
return False.
"""


def inherits_from(obj, a_class):
    """
    Function to know if the obj is a class or inherited class of a_class.
    """
    if issubclass(type(obj), a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False

# En este caso usamos la funcion: issubclass (tmb se podria haber usado isinstance() - pero la idea era probar
# issubclass en este ej). Le tuve que agregar el: type para el: obj porque sino me decia que True (ver ejemplo del
# main) no era una clase y al ponerle el type nos dice que es de clase: bool tomando el ejemplo que se usa en el
# archivo 4-main.py.
# Agregue lo de: and type(obj) is not a_class -> para que no nos de que como que bool es una sub clase de bool (osea
# del mismo tipo de dato), si no se ponia esto te decia que bool era una sub clase de bool.
