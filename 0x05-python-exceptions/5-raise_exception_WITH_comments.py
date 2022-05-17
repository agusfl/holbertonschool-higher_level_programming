#!/usr/bin/python3
"""
Function that raises a type exception.
"""


def raise_exception():
    raise TypeError

"""
Tanto este ejercicio como la task 6 son bastante faciles y parecidos. Aca lo que se hace es usar "levantar una exepcion"
(raise an exception) con la keyword "raise". Simplemente necesitamos usar la keyword raise y poner el tipo de excepcion
que estamos levantando, en este caso nos dicen que va a ser para una excepcion para: TypeError.
Podemos ver en el 5-main.py que cuando se llama a nuestra funcion (raise_exception) se va al bloque de codigo del
except TypeError y se ejecuta el mensaje que se puso en el codigo.
"""
