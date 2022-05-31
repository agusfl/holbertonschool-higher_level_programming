#!/usr/bin/python3
"""
Function that reads a text file (with UTF8 encoding) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function to read a file and print it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)

# Aca usamos las funciones de input/output, se usa "with" como se recomienda en la documentacion para que se encargue
# de cerrar el archivo correctamente una vez que se termine de leer o hacer lo que quiera con ese archivo.
# Usamos encoding utf-8 porque asi lo pide la letra.
# Guardamos en la variable creada "read_data" lo leido dentro del filename (que lo llamamos 'f') y despues con print
# printeamos lo que se leyo. 
