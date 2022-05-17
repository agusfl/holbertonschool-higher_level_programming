#!/usr/bin/python3
import sys
"""
Function that prints an integer.
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (Exception) as errors:
        sys.stderr.write("Exception: {}\n".format(errors))
        return False

"""
Este ejercicio es muy similar al ejercicio 1, con la diferencia de que se quiere imprimir un mensaje de error en el
standar error (stderr) para hacer esto hay que importar el modulo: sys y usar: stderr y write.
Lo distinto tmb de este ej es que use la excepcion generica: Exception para probar (tmb podria haber usado las
excepciones que habia usado en el ej 1) y usamos la keyword "as" para darle una alias al except y asi poder printear
el error correspondiente.
"""
