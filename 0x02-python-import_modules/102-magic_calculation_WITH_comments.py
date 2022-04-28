#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)

# Antes del ultimo return se podria poner un else: pero no es necesario, se puede hacer de esta manera y tmb queda
# bien. En este caso si entra en el if de 'a' menor a 'b' va a retornar y salir del programa y no va a llegar al
# ultimo return de sub(a, b) y si no entra en el if va a directo al return de sub(a , b), seria el mismo funcionamiento
# en caso que pusieramos el else antes del ultimo return e indentando dicho return para que quede dentro del "bloque"
# del else.
