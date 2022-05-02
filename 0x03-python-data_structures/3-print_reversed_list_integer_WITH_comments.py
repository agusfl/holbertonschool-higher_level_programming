#!/usr/bin/python3
"""
Function that prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse() # Usamos el reverse() method para reversear la lista "my_list". Aca ya dejamos la lista
    # reverseada y despues la recorremos con un for y la vamos imprimiendo.
    for i in my_list:
        print(f"{i}")
