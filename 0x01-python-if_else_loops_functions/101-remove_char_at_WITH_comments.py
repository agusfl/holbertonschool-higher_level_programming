#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str_copy = str[:n] + str[(n+1):]
    else:
        str_copy = str
    return str_copy

# Se indica que si el numero que nos pasan (n) es mayor o igual a cero entonces queremos copiar en un nuevo string todo
# el string (str) que nos pasan pero sin lo que este en la posicion (n) que nos pasen, por eso en el nuevo str_copy pongo
# que se tome con (slicing) las primeras posiciones del 'str' hasta uno antes de la posicion de la 'n' ya que :n no incluye
# al n y con el + se concatena lo que seria la segunda parte que es desde la posicion: n+1 del 'str' hasta el final (eso se
# indica con los ultimos dos puntos) de esta forma logramos diviendiendolo en dos partes y concatenando imprimir todo menos
# la posicion que se pasa con el 'n'. Despues en el else se indica que se imprima todo el string ya que por el main nos damos
# cuenta que cuando 'n' es negativo se quiere que se imprima todo el string completo.
# Por ultimo indicamos que se retorna la copia del string sin la posicion que se nos indique en el parametro 'n' de la
# solucion.
