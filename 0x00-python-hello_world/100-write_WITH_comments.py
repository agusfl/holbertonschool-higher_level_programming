#!/usr/bin/python3
import sys # importo la libreria sys para tener la funcion write

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19")
# "llamo" a la libreria sys que importamos despues con el .stderr le indico que quiero imprimir en el standard error
# y con el .write le indico que escriba el texto que nos piden en el ejercicio (usamos wirte en lugar de "print" porque
# la letra nos lo pide asi), el write no hace un salto de linea por default como el print, por lo tanto se lo agrego
# a continuacion:
sys.stderr.write('\n')
exit(1)
# Se indica que salga con un exit de 1 (como para indicarnos que hubo un error y no es 0).
