#!/usr/bin/python3
"""
Function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cont += 1
        except (TypeError, ValueError):
            continue
    print("")
    return cont

"""
Este ejercicio es muy parecido al cero, con la diferencia de que buscan que se genere un error en el programa (ver
archivo 2-main,py y su output) y pasan listas que no solo tienen numeros, sino que tmb strings, esto es para ver otros
tipos de errores ademas del IndexError. 
En este caso tenemos que usar un loop (usamos for) por fuera del "try" y el "except" y en lugar de manejar en el except el "IndexError" se manejan los errores de: TypeError y ValueError ya que son los dos tipos de errores que podrian suceder en este ejercicio. En el except ponemos un continue ya que si por ejemplo uno de los elementos de la lista que pasen
en "my_list" es distinto a un numero (como ser un string) queremos que se continue con el loop y no se haga nada mas,
por lo tanto "saltea" esa posicion con el continue y sigue para la proxima posicion de my_list, por ende solo vamos
a imprimir cuando sea un numero.
"""
