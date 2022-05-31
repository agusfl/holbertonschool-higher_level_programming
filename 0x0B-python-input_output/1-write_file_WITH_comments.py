#!/usr/bin/python3
"""
Function that writes a string to a text file (with UTD8) and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data

# En este ejercicio lo que hacemos es escribir dentro de un archivo txt (por lo tanto usamos el write)-
# Por eso con el with y el open abrimos lo que se pase en el primer argumento (filename) y le pasamos como opcion
# para intractuar con el archivo la 'w' que significa que queremos escribir dentro del filename (con la 'w' te sobre
# escribe el texto si ya hay algo).
# Despues creamos una variable llamada "write_data" para escribir en esa variable lo que se pase en el segundo
# argumento "text". Por ultimo retornamos write_data tal cual nos piden en la letra.
# Podemos ver que al hacer esto y usarlo con el archivo 1-main.py se crea un archivo llamado "my_first_file.txt" con el
# texto que le ponen en el archivo main. Al ejecutar el main se retorna el numero de palabras escritas y se crea el
# archivo que acabo de decir. El "filename" es el archivo donde se escribe el "text".
