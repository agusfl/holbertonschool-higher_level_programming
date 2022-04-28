#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 # Importamos hidden_4 ya que con el codigo de: curl ... que ponen en el ej 4 se importa el archivo desde
    # github.
    hidden = dir(hidden_4) # Hago una variable "hidden" donde guardo con la funcion dir() todo lo que haya en hidden_4
    # y una vez que lo tenemos en la variable lo podemos iterar e ir imprimiendolo.
    for i in hidden:
        if (i[0] != '_' and i[1] != '_'): # Ponemos esta condicion ya que nos piden que no se impriman las variables con
            # underscore (__) y esas variables arrancan con dos __ por lo tanto la posicion 0 y la 1 serian __ por eso
            # ponemos que si es distinto se imprima 'i' que esta dentro del for que recorre lo que esta en hidden.
            print(i)

# En internet vi que habia una solucion para hacerlo en una sola linea de codigo:
# El codigo seria:
# import sys
# print(f"{sum(int(num) for num in sys.argv[1:]))})
