#!/usr/bin/python3
"""
Module 5-text_indentation, this module has a function that prints
a text with 2 new lines after each of the following characters: . ? :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after the following
    characters: . ? :
    """
    if type(text) is not str: # Si el argumento que nos pasan "text" no es de tipo string entonces 'levantamos' el mensaje que
        # nos indican en la letra del ej.
        raise TypeError("text must be a string")
    else:
        characters = [".", ":", "?"] # Se hace una lista para iterar con los caracteres que si se encuentran en "text" hay que
        # poner 2 break lines ("\n") despues de que se encuentra alguno de estos tres caracteres.
        new_text = "" # Se crea una variable para almacenar el texto que vamos iterando de "text" y poder agregar los saltos de
        # linea cada vez que se encuentre alguno de los tres caracteres de la lista "characters".
        for element in text:
            new_text += element
            if element in characters:
                new_text += "\n"
                print(new_text.strip(" "))
                new_text = ""
        print(new_text.strip(" "), end="")

# Explicacion a partir del for: Se hace un for declarando una variable "element" para que se recorra cada elemento osea cada
# palabra que haya en el texto que nos pasen como argumento, al usar la "in" keyword lo que hace es recorrer cada elemento
# del texto. Despues se define que se va a ir guardando en la variable que creamos "new_text" cada elemento (palabra) que se
# vaya leyendo del "text" que nos pasen como argumento.
# En el if se establece la condicion qeu si el elemento es uno de los 3 que habiamos definido dentro de la lista "characters"
# vamos a agregar en "new_text" un salto de linea, luego vamos a imprimir lo que este almacenado usando el metodo .strip() para
# quitar los espacios en blanco tanto antes como despues que tenga el texto que se va a imprimiendo y despues se define a
# new_text = "" osea como un string vacio --> esto es como para "resetear" lo que hay dentro de new_text cada vez que hayamos
# encontrado uno de los caracteres dentro de characters (punto, dos puntos o un signo de pregunta), esto lo que va a hacer es
# imprmir todas las palabras o frases que esten antes de un punto, dos puntos o un signo de pregunta y va agrear el salto de
# linea, despues de imrpimir queremos resetear el contenido de new_text para que cuando se vuelva a iterar dentro del for element
# dentro del text no nos vuelva a imprmir el texto que ya imprimio antes sino que imprmia apartir de ahi.
# Por ultimo se agrega un ultimo print alfinal por fuera del for para que se impriman los elementos del texto que no tengan
# ninguno de los caracteres dentro de "characters".
