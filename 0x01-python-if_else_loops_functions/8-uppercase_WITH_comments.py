#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print(f"{i}", end='')
    print()

# Se hace un for para recorrer el string (str) que se pase como argumento a nuestra funcion 'uppercase' y dentro
# del for se evalua con un if si la letra del string que esta en la posicion 'i' esta dentro del rango: 97 a 122
# entonces significa que la letra es minuscula (lowercase) por lo tanto la transformamos a mayuscula, esto se hace
# restando 32 (ya que la diferencia en la tabla ASCII entre las letras minusculas y las mayusculas siempre es 32) a
# la letra que este en la posicion que estamos evaluando (la posicion esta marcada por 'i'), asu vez transformamos
# i a character usando la funcion: chr y eso es lo que mandamos a imprimir al primer print.
# Por ultimo agregamos un print vacio para que se imprima un salto de linea al final ya que en el primer print
# cambiamos el 'end' para que sea sin espacios y sin salto de linea, para que pueda imprimir toda la palabra junta
# y no una letra por fila.
