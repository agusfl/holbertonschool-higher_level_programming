#!/usr/bin/python3
"""
Function that finds the biggest integer of a list.
"""


def max_integer(my_list=[]):
    if not my_list: # Chequeamos caso de letra, si la lista no existe que se retorne None.
        return None
    else:
        max_number = my_list[0] # Definimos max number como el elemento 0 de la lista "my_list".
        for i in my_list: # iteramos la lista.
            if i > max_number: # Si i es mayor a max_number entonces queremos que max_number pase a ser 'i' asi es
                # el numero mas grande de la lista, esto lo hacemos iterando toda la lista asi nos aseguramnos que
                # nos vamos a quedar con el numero mas grande almacenado en la variable creada "max_number".
                max_number = i
        return max_number # retornamos el max number.
