#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
        return list(map(lambda x: x * number, my_list))

# Se nos indica en la letra que esta funcion no puede tener mas de 3 lineas, por eso se hace de esta forma.
# Al usar la funcion: list() se retorna una nueva lista. Tambien se usa la funcion: map() con "lamda function"
# para multiplicar cada valor de la lista "my_list" por el "number" que se pase como argumento en nuestra funcion.
# Como ya vimos el primer argumento de map es la funcion que queres aplicar a una secuencia, y el segundo argumento
# es la secuencia en la cual se quiere aplicar la funcion.
