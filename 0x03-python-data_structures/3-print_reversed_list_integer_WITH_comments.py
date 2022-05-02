#!/usr/bin/python3
"""
Function that prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse() # Usamos el reverse() method para reversear la lista "my_list". Aca ya dejamos la lista
        # reverseada y despues la recorremos con un for y la vamos imprimiendo.
        for i in my_list:
            print(f"{i}")

# Esta era una version de codigo que andaba pero el checker daba problemas, para solucionarlo tuve que usar
# reversed en lugar de reverse asi: 
# for i in reversed(my_list):
