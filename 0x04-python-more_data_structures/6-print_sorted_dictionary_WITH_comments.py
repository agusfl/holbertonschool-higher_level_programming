#!/usr/bin/python3
"""
Function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary): # Se hace un for para recorrer el diccionario e imprimirlo.
        print(f"{key}: {a_dictionary[key]}")

# Definimos "key" dentro del for para iterar el diccionario por lo tanto "key" seria la key del diccionario (valga
# la redundancia) y "a_dictionary[key]" seria el "value" de la "key".
