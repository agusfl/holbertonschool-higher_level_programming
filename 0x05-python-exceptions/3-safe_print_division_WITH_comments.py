#!/usr/bin/python3
"""
Function that divides 2 integers and prints the result.
"""


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

"""
En este ejercicio se analiza y maneja otro tipo de except, el de: ZeroDivisionError --> esto sucede cuando se quiere
dividir un numero entre cero.
No tenemos que castear "a" y "b" a integers ya que la letra nos dice que podemos asumir que van a ser integers (osea
solo nos van a pasar numeros en los archivos de prueba).
Otra de las cosas nuevas que se implementan en este ejercicio es el uso del "finally", el finally lo que nos permite
es ejecutar el codigo que se ponga adentro siempre, independientemente de lo que se ponga en el try y en el except.
En este caso lo que queremos ejecutar en el bloque de codigo del try es la division entre "a" y "b" y si pasa el error
de que "b" sea igual a 0 queremos que se ejecute lo que este dentro del bloque de codigo del except (ya que no se puede
dividr entre 0) y por ultimo siempre queremos que se imprima el resultado, en caso de que se pueda dividir vamos a
querer que se imprima el resultado de dicha division y si no se puede dividir porque "b" es cero, vamos a querer que
se imprima que el resultado es: None. Por ultimo retornamos el resultado sea cual sea.
"""
