#!/usr/bin/python3
"""
Module for creating a class: Base
"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute __nb_objects if there is
        no id and set it as id.
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes and
        to avoid duplicating the same code (by extension, same bugs)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.
        Update the class Base by adding the static method
        def to_json_string(list_dictionaries -> dictionary): that returns the
        JSON string representation of list_dictionaries static method es un
        metodo que se puede usar por fuera de la clase, es parecido a definir
        una funcion normal.
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = [] # si es None o esta vacia, ponemos lo que nos indica la condicion de letra devolver el string dentro de []
        return json.dumps(list_dictionaries) # esto retorna el objeto json en formato string