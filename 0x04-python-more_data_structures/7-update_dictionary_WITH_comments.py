#!/usr/bin/python3
"""
Function that replaces or adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    new_key_value = {key: value} # Se crea un nuevo conjunto de key/value, con lo que se pase como argumentos de nuestra
    # funcion que estamos creando: "update_dictionary".
    a_dictionary.update(new_key_value)
    return a_dictionary

# Uso el metodo "update", el mismo nos permite actualizar un diccionario agregando info nueva, comos ser el nuevo par
# de key value que creamos y almacenamos en "new_key_value" y tambien nos permite sobreescribir "keys" ya existentes
# por lo tanto si se pasa una key que ya existe con un valor distinto, el metodo update nos va a permitir actualizarlo
# en el diccionario.
