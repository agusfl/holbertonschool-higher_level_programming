#!/usr/bin/python3
"""
Function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):
    try:
        print(f"{value:d}") # La letra nos dice que printemos de esta manera, ponemos para que se imprima el "value"
        # que va a ser lo que se pase en el 1-main.py y le ponemos el :d para castearlo a que imprima en decimal.
        return True # Retornamos True en este caso.
    except (TypeError, ValueError):
        return False # Retornamos falso en caso de que no sea un integer, en el 1-main.py si se pone: if not has_been_print se esta entrando en este caso cuando es falso.
