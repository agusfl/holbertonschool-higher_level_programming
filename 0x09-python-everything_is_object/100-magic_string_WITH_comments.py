#!/usr/bin/python3
def magic_string(string_list=[]):
    string_list += ["BestSchool"]
    return ', '.join(string_list)

# En esta funcion lo que se hace es tomar una lista llamda "string" como argumento de: magic_string y dentro de la
# funcion se indica que se vaya agregarndo la palabra: "BestSchool" dentro de nuestra lista "string_list" para que
# se imprima la cantidad de veces que se indique en el loop del archivo: 100-main.py.
# Por ultimo en el return usamos el metodo "join" para sacarle los [] cuando se imprime y le ponemos solo una coma
# y un espacio.
