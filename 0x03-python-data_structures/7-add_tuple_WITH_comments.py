#!/usr/bin/python3
"""
Function that adds 2 tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0) # Esto es para el caso de letra que nos ponen de si la tupla que le vas a sumar tiene menos de
    # 2 elementos, en dicho caso se quiere que se sume el valor de 0 para el elemento que falte. En caso de que
    # se pase un numero como en el segundo ejemplo del archvio main que pasan: (1, 0) el uno suplanta al primer 0
    # que tenemos aca y como no se puso nada en el segundo elemento de la tupla: (1, 0) se pone va a sumar el 0 que
    # habiamos puesto aca: (0, 0).
    tuple_b += (0, 0) # Idem caso anterior.
    result1 = tuple_a[0] + tuple_b[0] # Sumo los primeros elementos de cada tupla en una variable llamada "result1"
    result2 = tuple_a[1] + tuple_b[1] # Sumo los segundos elemenots de cada tupla en una variable llamada "result2"
    new_tuple = (result1, result2) # Creo una nueva tupla con las dos variables que cree que tienen la suma de los
    # elementos de las tuplas que nos pasan como argumentos: 'tuple_a' y 'tuple_b'.
    return new_tuple # Se retorna la nueva tupla, tomar en cuenta que las tuplas a diferencia de las listas son
 # inmutables (al igual que los strings).

 # Para el caso de que la tupla sea mayor a dos tomar solo los primeros dos integers, no hay que poner ninguna
 # condicion en el codigo ya que es lo que se va a hacer por defecto.
