#!/usr/bin/python3
"""
Function that deletes the item at a specific position in a list.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx] # Usamos el "del" statement para borrar el elemento idx de la lista my_list.
        return my_list
