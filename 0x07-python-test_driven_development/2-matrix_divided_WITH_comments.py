#!/usr/bin/python3
"""
Module 2-matrix_divided, this module has a function that divides all
elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """

    # Analizamos los casos de letra, si el tipo de dato que se pasa no es una list y si los elementos 
    # de las listas que conforman la matrix no son integers o floats.
    # Tambien se chequea que el len(matrix[0]) == 0 para evaluar si la lista que se pasa esta vacia.
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [] 
    # Se crea una matrix vacia para completarla con el resultado de dividir cada elemento de la matrix
    # entre el numero que se pase en: div
    for lists in matrix:
        # Se hace un for que recorra todas las listas que esten dentro de la matrix y en caso que las listas no sean
        # de tipo "list" se levanta (raise) un mensaje de error 
        if type(lists) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            if len(lists) != len(matrix[0]):
    # len matrix[0] es el largo de la primer lista de la matrix, seria 3
    # en el caso del main de prueba.
            raise TypeError("Each row of the matrix must have the same size")
        new_list = [] # Creamos una lista vacia donde vamos a ir guardando con el metodo append el nuevo resultado
        # que va a ir en la lista, osea el elemento dividido el numero que se pase en "div".
        for position in lists: # "position" seria cada elemento y lo vamos a dividir por "div".
            if type(position) is not int and type(position) is not float:
            # Si el tipo de position no es int o float hacemos un raise de TypeError con el mensaje que nos dicen
            # en la letra.
                raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            new_list.append(round(position/div, 2))
        new_matrix.append(new_list)
    return new_matrix
