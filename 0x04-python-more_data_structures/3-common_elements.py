#!/usr/bin/pyton3
"""
Function that returns a set of common elements in two sets.
Uso la funcion "intersection" para sacar los datos iguales de ambos sets.
En este ej tmb se podria usar el operador & de la
siguiente manera --> return set_1 & set_2
"""


def common_elements(set_1, set_2):
    return set_1.intersection(set_2)
