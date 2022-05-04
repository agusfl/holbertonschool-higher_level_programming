#!/usr/bin/python3
"""
Function that adds all unique integers in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    unique_my_list = set(my_list) # Usamos set para quitar los elementos duplicados de la lista.
    return sum(unique_my_list) # Usamos la funcion "sum" para sumar todos los elementos de la lista y lo retornamos.
