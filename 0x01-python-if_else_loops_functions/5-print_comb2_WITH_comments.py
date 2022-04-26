#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(f"{i:02d}")
    else:
        print(f"{i:02d}", end=', ')

# Con el :02d --> le indico que quiero imprimir el numero con dos digitos, se hace un if para que si 'i' es 99 (que es
# el ultimo numero) que imprima sin coma y espacio y que lo haga con un salto de linea (que viene por default en print)
# y si 'i' no es 99 entonces que imprima el numero con la coma y el espacio tal cual pide la letra del ej.
