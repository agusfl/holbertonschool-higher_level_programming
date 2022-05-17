#!/usr/bin/python3
"""
Function that raises a name exception with a message.
"""


def raise_exception_msg(message=""):
    raise NameError(message)

"""
Como adelante en los comentarios del ejercicio 5, este ej es muy similar simplemente que en esdte caso usamos raise
para el except de: NameError y con el mensaje que se pase como argumento a nuestra funcion en "message".
"""
