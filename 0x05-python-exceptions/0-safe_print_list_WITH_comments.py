#!/usr/bin/python3
"""
Function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        while cont < x:
            print(f"{my_list[cont]}", end="")
            cont += 1
    except IndexError:
        pass
    print("")
    return cont

"""
En este ejercicio lo que se esta buscando es poder imprimir todos los numeros que nos pasen en el argumento "my_list"
en una misma fila (sin salto de linea, por eso ponemos: end="") y nos pasan un segundo argumento "x" que nos indica
el numero de elementos a imprimir, la idea del ejercicio es que "x" puede ser mayor a la cantidad de elementos que tenga
la lista "my_list" por lo tanto el error que nos saldria si quisieramos imprimir un elemento por fuera del numero de
elementos de "my_list" nos saldria un "IndexError" ya que se quiere acceder a una secuencia con un indice que no existe.
Por lo tanto lo que hacemos es usar el "try" y el "except" para poder manejar dicho error y que no se "rompa" nuestro
programa al ejecutarse debido al IndexError.
Lo que hacemos es poner dentro del "try" el codigo que queremos que se ejecute, en este caso se pone un while para
recorrer toda la lista y vamos imprimiendo todos los numeros que esten en ella en una misma linea, 
con el siguiente codigo: print(f"{my_list[cont]}", end=""), y con cont += 1 incrementamos la variable cont para que
se recorra todos los elementos de la lista hasta que sea menor a "x" ya que es hasta donde podemos imprimir.
Cuando se llegue a la posicion que supera la cantidad de elementos de "my_list" se va a entrar en el except, al mismo
le aclaramos que estamos modificando el comportamiento para el "IndexError" ya que sabemos que ese es el error que iba
a dar (lo teniamos que poner asi tmb porque sino el PEP8 (pycodestyle) nos daba error sino especificabamos cual
exception estamos tratando). Igualmente cuando no se sabe que exception va a ser se puede usar la excpetion generica:
"Exception" ya que todas las excepciones se heredan de Exception. Dentro del exception ponemos que lo que queremos que
se haga es nada.. y esto lo indicamos con --> pass.
Por ultimo retonramos la variable cont que nos sirvio de contador para ver cuantos elementos se imprimieron. 
--> Tomar en cuenta que esto se podria haber solucionado de distintas maneras pero nosotros no podiamos por condiciones
de letra importar ningun modulo ni usar la funcion: len().
"""

#--> Esta es una segunda forma de hacer el ejercicio usando el while por fuera del try y con break (para salir del
# while) en lugar del pass.
"""
def safe_print_list(my_list=[], x=0):
    cont = 0
    while cont < x: # se ejecuta el try y el except siempre y cuando nuestra variable "cont" sea menor al x que pasan como argumento para imprimir la cantidad "x" de numeros que se pasen en la lista "my_list" (1er argumento).
        try:
            print (f"{my_list[cont]}", end="") 
        except IndexError:
            break
        cont += 1
    print ("")
    return cont

--> Hacemos un while por fuera del try y el except para usar el break en el except en lugar del pass, esto es asi
ya que tanto el break como el continue solo se pueden usar dentro de un loop.
Sacando esto, la solucion y explicacion de la misma es identica a la anterior.

# Usamos el try y el except tal cual nos indican en la letra, adentro del try ponemos que se imprima la posicion "i"
# de la lista my_list, ponemos end="" para que se imprima todo en la misma linea sin que se haga un salto de linea.
# En el except le tenemos que especificar el nombre de error que vamos a manejar, ejemplo si es un error de tipo va a
# ser TypeError, etc.. En este caso el error va a ser de IndexError (se puede ver la lista de standard exceptions)
# En este caso ponemos un break en el except ya que cuando no se entre en el try, si en el "x" que pasan es mayor
# al largo de la lista y en ese caso queremos que haga un break. En la variable que creamos "i" la hacemos como contador
# para retornar la cantidad de elementos que se imprimieron.
"""
