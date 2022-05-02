#!/usr/bin/python3
"""
Function that prints a matrix of integers.
"""

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]: # Se pone -1 para que no se imprima con espacio en el ultimo elemento de
                # la fila.
                print(f"{i}", end= " ")
            else:
                print(f"{i}", end="") # Esto es para el ultimo elemento de la fila, queremos que se imprima pero
                # sin un espacio al final.
        print() # Esto es para que nos imprima un salto de linea despues de cada fila.
