#!/usr/bin/python3
"""
Function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = [] # Creamos una nueva lista para retornar y almacenar los valores que guardamos en la
    # variable "div".
    for i in range(list_length): # Recorremos el largo que se pase en la variable "list_length" (tecer
        # argumento) ya que esta variable es la que indica cuantos elementos se van a imprimir.
        try:
            div = my_list_1[i] / my_list_2[i] # Dividimos cada posicion de ambas listas entre si y guardamos el
        # resultado en la variable creada "div" (esta variable es la que vamos a agregar con append en la nueva lista).
        except TypeError: # Si se pasa un dato que no sea integer queremos imprimir el siguiente mensaje.
            div = 0 # En la letra dice que se devuelve 0 en cada caso en los que hay una excepcion,
            # dice: If 2 elements can’t be divided, the division result should be equal to 0.
            print("wrong type")
        except ZeroDivisionError: # Si se quiere dividir entre 0, ponemos el siguiente mensaje en su correspondiente
            # exception --> ZeroDivisionError.
            div = 0
            print("division by 0")
        except IndexError: # Si el numero que se quiere imprimir esta fuera del rango imprimimos el siguiente texto
            # esto lo hacemos como ya vimos en otros ejercicios manejando la exception --> IndexError.
            div = 0
            print("out of range")
        finally:
            new_list.append(div) # Con append vamos agregando los resultados en la nueva lista que
            # creamos, recordar que en finally se ejecuta siempre.
    return new_list # Por ultimo retornamos la nueva lista.
