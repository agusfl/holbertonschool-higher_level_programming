#!/usr/bin/python3
"""
Function that computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    if matrix is None: # Considero el caso de que la lista que nos pasen sea vacia, en dicho caso retornamos None.
        return None
    else:
        new_matrix = [] # Se crea una lista nueva para almacenar los resultados, tal cual se pide en la letra (no
        # modificar la matriz original.
        for rows in matrix: # Se hace un for para recorrer lo que seria cada fila de la matriz que pasen.
            new_matrix.append(list(map(lambda x: x * x, rows))) 
            # Se agrega los datos a la nueva lista (con append) y se usa la funcion map con lambda para aplicar
            # la "funcion sin nombre (lambda)" para hacer el cuadrado de los numeros que esten en la matriz y
            # como segundo argumento se le pasa "rows" para que lo haga en cada fila.
        return new_matrix
