#!/usr/bin/python3
"""
Function that removes all characters c and C from a string.
"""


def no_c(my_string):
    new_string = "" # Creo un nuevo string vacio para ir completandolo mas adelante con todas las letras que nos pasen
    # en "my_string" menos las letras: 'c' y 'C' desde el archivo main.
    for i in my_string: # Hago un for para recorrer my_string e ir completando "new_string".
        if i != 'c' and i != 'C': # Aca tmb se podria poner: if i not in 'cC. En esta parte del codigo es que le indico
            # que no se guarden las letras 'c' o 'C'.
            new_string = new_string + i # Voy guardando las letras que se van iterando en 'i', pongo "new_string" + "i"
            # para que se vaya concatenando todas las letras que se guardan.
    return new_string # Devolvemos el nuevos string sin las letras 'c' o 'C'.
