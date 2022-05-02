#!/usr/bin/python3
"""
Function that retrieves an element from a list line in C.
"""


def element_at(my_list, idx):
    if idx < 0:  # Analizo caso de letra de si el indice que pasan para buscar es negativo, al poner solo return en
        # python devuelve "None" (que es lo que nos piden en la letra) por defecto.
        return
    elif idx > len(my_list): # Analizo el otro caso de letra de si el idx esta fuera del rango de la lista, esto
        # lo puedo hacer con la funcion "len" ya que len me dice el largo de la lista, entonces si idx es mayor a eso
        # significa que esta fuera de rango.
        return
    # Una vez que ya analice los dos casos "border" por decir de alguna manera, paso a hacer el for loop para buscar
    # el indice que el usaurio indique en el archivo main y retornar su valor.
    else:
        return my_list[idx] # retornamos el elemento que este en la posicion "idx" de la lista "my_list".

# Se podria optimizar los primeros dos if poniendo un "or" y las dos condiciones juntas.
