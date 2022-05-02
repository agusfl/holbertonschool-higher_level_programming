#!/usr/bin/python3
"""
Function that replaces an element of a list at a specific position (like in C).
"""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
      #  for i in my_list: -> Esta era una alternativa que habia hecho como primer opcion pero me di cuenta que no es
      # necesario hacer un for ni la condicion del if que pongo mas abajo comentada.
       #     if i == idx:
                my_list[idx] = element
                return my_list

# Es muy parecido al ejercicio 1, salvo que aca se quiere cambiar el elemento que este en la posicion especificada
# por el valor que nos pasen en el tercer argumento de nuestra funcion "replace_in_list" que seria el argumento:
# "element". Y cambian un poco los return de los casos "border".
