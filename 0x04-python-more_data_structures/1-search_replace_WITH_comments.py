#!/usr/bin/python3
"""
Function that replaces all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    if my_list is None: # Se valida que la lista no este vacia.
        return None
    else:
        new_list = [] # Se crea una nueva lista para no modificar la original.
        for i in my_list:
            if i == search:
                new_list.append(replace)
            else:
                new_list.append(i)
        return new_list

# Se hace un for para recorrer la lista que nos pasan y si se encuentra el elemento que se quiere cambiar (search)
# se lo modifica por replace (que seria el nuevo elemento). Aca lo que se busca es que si esta el numero "search"
# en la lista se modifique por lo que se pase como argumento en "replace". Usamos el metodo append para ir agregando en
# la nueva lista creada (new_list) los valores, con el else se agregan todos los valores que no se cambien y en el if
# se contempla el caso de cambiar el valor de "search" por "replace".
