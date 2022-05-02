#!/usr/bin/python3
"""
Function that retrieves an element from a list line in C.
"""


def element_at(my_list, idx):
    if idx < 0:  # Analizo caso de letra de si el indice que pasan para buscar es negativo, al poner solo return en
        # python devuelve "None" (que es lo que nos piden en la letra) por defecto.
        return
    elif idx >= len(my_list): # Analizo el otro caso de letra de si el idx esta fuera del rango de la lista, esto
        # lo puedo hacer con la funcion "len" ya que len me dice el largo de la lista, entonces si idx es mayor a eso
        # significa que esta fuera de rango.
        # Hay que poner mayor o igual al largo de la lista ya que la funcion len() no cuenta desde 0 ejemplo si la
        # lista tiene 3 elementos te va a retornar: 3 y no 2 como si fuera: 0 1 2. Y si la lista tiene 3 elementos
        # y queres acceder al ultimo elemento ese estaria en la posicion 2 y no en la 3, por lo tanto hay que poner
        # el mayor o IGUAL ya que si quisieras acceder a la posicion 3 estarias "out of range".
        return
    # Una vez que ya analice los dos casos "border" por decir de alguna manera, paso a hacer el for loop para buscar
    # el indice que el usaurio indique en el archivo main y retornar su valor.
    else:
        return my_list[idx] # retornamos el elemento que este en la posicion "idx" de la lista "my_list".

# Se podria optimizar los primeros dos if poniendo un "or" y las dos condiciones juntas.
