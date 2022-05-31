#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each line containing a
specific string (see holberton example).
"""


def append_after(filename="", search_string="", new_string=""):
    """Implementation of function to insert a line of text after each line
    containing a specific string."""
    with open(filename, 'r+') as f:
        # r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
        # a+: Opens a file for both appending and reading.
        # En este caso necesitamos leer y poder escribir por eso no usamos a+
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0) # usamos el metodo seek() para setear la posicion del file 'f' que seria "filename" en 0 para que
        # arranque a escribir desde el inicio.
        f.write(new_text) # escribimos lo que esta dentro del nuevo texto ("new_text") dentro del file 'f' que es
        # el que hay que devolver.

# Creamos un string "new_text" donde vamos a guardar el texto que se vaya leyendo y en los casos que "search_string"
# que es el string que se pasa en el segundo argumento de la funcion y es la palabra que hay que buscar en el texto
# del "filename" en el caso del 100-main.py podemos ver que ese texto es el que nos pasan en el
# archivo: append_after_100.txt, una vez que se encuentra esa palabra en el texto ("line" seria cada string que se
# va leyendo dentro del filename ('f' ya que le pusimos el as para renombrarlo)) queremos cambiarla por lo que se
# pase en el tercer argumento de la funcion que estamos creando "append_after" que seria "new_string", entonces
# lo sumamos a nuestro nuevo texto ("new_text"). 
