#!/usr/bin/python3
"""
Function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):
    try:
        print(f"{value:d}") 
# La letra nos dice que printemos de esta manera (con .format y :d (decimal)), ponemos para que se imprima el "value"
# que va a ser lo que se pase en el 1-main.py y le ponemos el :d para castearlo a que imprima en decimal (int).
        return True 
# Retornamos True tal cual nos indica la letra si el "value" se pudo imprimir correctamente.
    except (TypeError, ValueError):
        return False
# En este caso en el except vamos a manejar los dos tipos de error que nos saldrian en esta ocacion que son de 
# TypeError (por que en value se nos puede pasar algo que no sea un numero, como ser un string) y el ValueError en
# caso de que se pase un numero invalido (ejemplo: si se quiere pasar la raiz negativa de un numero (no existe)).
# Retornamos False como nos indica la letra, en el 1-main.py podemos ver que cuandos ponen: if not has_been_print 
# se esta entrando en este caso, cuando es falso.
