#!/usr/bin/python3

"""
Function that deletes keys with a specific value in a dictionary.
"""


def complex_delete(a_dictionary, value):
    copy_dictionary = a_dictionary.copy()
    for key, value_iter in copy_dictionary.items():
        if value_iter == value:
            del a_dictionary[key]
    return a_dictionary

# Se crea una copia del diccionario para no modificar el original, iteramos en la copia y borramos en el diccionario
# original. Usamos el metodo items() (que ya habia usado en el ejercicio 9) para poder trabajar con las "keys" y los
# "values" de nuestros diccionarios.
# Lo que hacemos en el for es ver si la variable que creamos "value_iter" dentro del diccionario que creamos como una
# copia de "a_dictionary" es igual al "value" que se pasa como argumento indicamos que se borre (con el metodo del)
# la "key" del diccionario original ("a_dictionary") y por ultimo ponemos que se retorne el diccionario original.
# En caso de que no se pase ningun valor dentro del argumento "value" se va a retornar el diccionario tal y como
# estaba ya que el return esta indentado de tal forma para que se cumpla siempre.
