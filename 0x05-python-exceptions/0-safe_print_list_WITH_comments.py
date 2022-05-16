#!/usr/bin/python3
"""
Function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x: # se ejecuta el try y el except siempre y cuando nuestra variable "i" sea menor al x que pasan para
        # imprimir la cantidad "x" de numeros que pasen en la lista "my_list".
        try:
            print (f"{my_list[i]}", end="") 
        except IndexError:
            break
        i += 1
    print ("")
    return i

# Usamos el try y el except tal cual nos indican en la letra, adentro del try ponemos que se imprima la posicion "i"
# de la lista my_list, ponemos end="" para que se imprima todo en la misma linea sin que se haga un salto de linea.
# En el except le tenemos que especificar el nombre de error al que se va a ir, ejemplo si es un error de tipo va a
# ser TypeError, etc.. En este caso el error va a ser de IndexError (se puede ver la lista de standard exceptions)
# En este caso ponemos un break en el except ya que cuando no se entre en el try, si en el "x" que pasan es mayor
# al largo de la lista y en ese caso queremos que haga un break. En la variable que creamos "i" la hacemos como contador
# para retornar la cantidad de elementos que se imprimieron.
