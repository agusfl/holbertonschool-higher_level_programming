#!/usr/bin/python3
"""
Module: 1-my_list
Has a class MyList that inherits from list
"""


class MyList(list):

    """
    Class MyList is a sub class of list.
    """
    def print_sorted(self):
        """
        Public instance method that prints the list sorted(ascending sort)
        """
        print(sorted(self))

# Cuando ponemos: print(sorted(self)) con el "self" hacemos referencia a la parent class "list", por lo tanto cuando
# en el archivo 1-main.py van agregando datos con "append" en my_list, esos son los datos que estamos usando aca con
# self, cuando ponemos sorted(self) los datos que se estan ordenando son esos.
# De esta forma estamos "extendiendo" la built-in class "list" agregando una sub clase (MyList) que imprime en
# pantalla una lista de numeros en orden ascendente. 
# Usamos la funcion: sorted()
# Tambien podriamos usar el metodo: sort() -> creando una lista nueva: new_list = self[:] y despues: new_list.sort()
