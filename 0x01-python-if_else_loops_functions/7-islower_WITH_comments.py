#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False

# 97 es la 'a' minuscula en ASCII y 122 es la 'z' pero pongo 123 ya que range toma hasta un valor menos que lo
# que se indica, por lo tanto al poner 123 va a tomar hasta 122.
# ord --> es una funcion que retorna el valor en ASCII del string o caracter que se le pase. Por lo tanto con el
# if estamos poniendo una condicion para evaluar que si el caracter (c) que nos pasaron como argumento de nuestra
# funcion 'islower' esta dentro del rango que marcamos que seria de la 'a' a la 'z' entonces que se retorne True
# ya que va a ser una letra minuscula y sino que se retorne Fasle.
