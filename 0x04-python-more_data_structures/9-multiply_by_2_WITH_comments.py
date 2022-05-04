#!/usr/bin/python3
"""
Function that returns a new dictionary with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    new_dictionary = {} # Se crea un nuevo diccionario tal cual nos indica la letra del ej.
    for key, value in a_dictionary.items():
        mul_by_2 = value * 2
        temp_dict = {key: mul_by_2}
        new_dictionary.update(temp_dict)
    return new_dictionary

# Recorremos con el for el diccionario usando el metodo items() para que nos permita iterar tanto por las "keys" como
# por los "values" del diccionario, creamos dos variables: "key" y "value" podrian tener otro nombre, les puse asi
# ya que representan las keys y values del diccionario. Creo una variable "mul_by_2" para almacenar el resultado
# de multiplicar al value por 2, eso lo guardo dentro de un directoprio temporal "temp_dict" y la key le asigno la
# que se este iterando ya que no hay que cambiar a la key.
# Uso el metodo update para agregar los elementos en el nuevo diccionario (recordar que con diccionarios no se puede
# usar el metodo append, por eso usamos update).
