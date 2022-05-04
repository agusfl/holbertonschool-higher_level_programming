#!/usr/bin/python3
"""
Function that returns a key with the biggest integer value.
"""


def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)

# Se usa la funcion "max" y "get".
# Al poner: if a_dictionary: --> se evalua si el diccionario existe, no es necesario poner un else con return None
# porque se toma en cuenta ya en la funcion max de por si, si ponia un else con el return None, el output me daba
# bien cuando ejecutaba el codigo en consola pero el checker daba un output mal.
# Por mas info ver: https://pythonguides.com/python-find-max-value-in-a-dictionary/#:~:text=In%20Python%20to%20find%20the,the%20highest%20value%2C%20the%20dict.
