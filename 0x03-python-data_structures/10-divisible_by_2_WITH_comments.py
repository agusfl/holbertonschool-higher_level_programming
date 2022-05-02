#!/usr/bin/python3
"""
Function that finds all multiples of 2 in a list.
"""


def divisible_by_2(my_list=[]):
    new_list = [] # creo una nueva lista vacia para ir completando con los valores True y False, True si es divisible
    # entre 2 y Flase si no es.
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True) # Uso el metodo append() para agregarle True a la lista cuando la posicion
            # 'i' es divisible entre 2.
        else:
            new_list.append(False) # Idem pero ponemos Flase en caso de que la posicion 'i' no sea divisible entre 2.
    return new_list # retorno la nueva lista con los valores True y False

# Otra forma de solucionarlo sin usar el metodo append podria ser:

"""
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = my_list.copy()
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                new_list[i] = True
            else:
                new_list[i] = False
        return new_list
""".
