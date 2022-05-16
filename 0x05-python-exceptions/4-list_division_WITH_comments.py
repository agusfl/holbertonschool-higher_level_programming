#!/usr/bin/python3
"""
Function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = [] # Creamos una nueva lista para retornar y almacenar los valores que guardamos en la
    # variable "div".
    for i in range(list_length): #Recorremos el largo que se pase en la variable "list_length" (tecer
        # argumento).
        try:
            div = my_list_1[i] / my_list_2[i] # dividimos cada posicion de ambas listas entre si.
        except TypeError:
            div = 0 # En la letra dice que se devuelve 0 en cada caso en los que hay una excepcion,
            # dice: If 2 elements can’t be divided, the division result should be equal to 0.
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list.append(div) # Con append vamos agregando los resultados en la nueva lista que
            # creamos, recordar que en finally se ejecuta siempre.
    return new_list # Por ultimo retornamos la nueva lista.
