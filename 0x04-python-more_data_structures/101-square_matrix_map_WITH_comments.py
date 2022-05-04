#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda x2: x2 * x2, x)), matrix))

# En el ejercicio nos piden basicamente que hagamos lo mismo que en el ejercicio 0 pero solo con tres lineas de codigo
# usando la funcion "map" y sin poder usar ningun loop.
# Por lo tanto usamos las funciones: list(), map() y lambda - la funcion list la usamos para crear y devolver una nueva
# lista, tal cual lo pide la letra, la funcion  map la usamos para aplicar la funcion que pongamos con "lambda" en
# toda la secuencia que va a ser la matrix al fin y al cabo.
# En el primer lambda indicamos que vamos a usar la variable 'x' y expresion (de la funcion lambda) indicamos que
# vamos a crear otra lista (esta lista junto con la primera que ya creamos van a formar nuestra matrix) para que 
# podamos iterar la matrix despues y hacer el cuadrado de todos los numeros dentro de la matrix.
# En el segundo "map" que usamos le indicamos que el segundo argumento (que seria la secuencia a la que se le va a
# aplicar la funcion (primer argumento de map)) es x (que viene del primer lambda que usamos) la secuencia va a ser x.
# Esto va a hacer que se aplique tanto a las filas que tenga la matriz como a las columnas.
# Despues de haber hecho todo esto recien podemos indicar como segundo argumento del primer "map" una matriz (seria
# las dos listas que creamos).
