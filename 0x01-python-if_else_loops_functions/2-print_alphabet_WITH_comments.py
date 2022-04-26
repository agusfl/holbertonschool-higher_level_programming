#!/usr/bin/python3
for i in range (97, 123):
    print(f"{chr(i)}", end='')
# El abecedario en minuscula en ascii arranca en: 97 y termina en 122 (pongo 123 porque el range no agarra el ultimo
# valor) dentro del formating (f) en el print casteo la variable 'i' a char poniendole: chr(i), por otro lado
# le saco el salto de linea que tiene el print por default y pongo para que este vacio asi me lo imprime todo junto
# El checker esta con problemas por el tema de que se va a empezar a usar el formato: f-string con el print en lugar
# del .format..
