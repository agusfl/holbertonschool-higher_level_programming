#!/usr/bin/python3
import sys
"""
Function that executes a function safely.
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
# "fct" es un puntero a una funcion y la funcion es la que este dentro de "*args", por lo tanto le pasamos *args como 
# argumento a fct y almacenamos el resultado en una variable llamada "result" para poder retornarla.
        return result
    except Exception as errors:
        sys.stderr.write("Exception: {}\n".format(errors))
        return None
# En caso que haya una excepcion que se escriba el mensaje de error (mismo que ejercicio anterior (7)) y que se retorne
# None.
