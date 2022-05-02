#!/usr/bin/python3
"""
Write a function that replaces an element in a list at a specific position without modifying the original list.
"""


def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0 or idx > len(copy_list):
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list

# Este es igual al ejercicio 2 solo que usamos una copia en lugar de la lista original, hacemos la copia de la lista
# usando el metodo: copy().
# En este ej lo podria haber hecho de la misma manera que el 2 cambiando todo por copy_list como aca pero decidi
# hacerlo de esta manera (habia puesto en los comentarios dle ej 1 que habia otras opciones de codigo mas cortas, como
# ser esta que use aca).
