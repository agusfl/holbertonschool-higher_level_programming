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
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation of list_objs
        to a file.
        A classmethod it can access class attributes, but not the instance
        attributes.
        Lo que se hace en esta funcion es cargar los objetos dentro de una
        lista, convertir esa lista de objetos en una lista de diccionarios
        y mandar dicha lista como argumento a la funcion "to_json_string"
        que creamos mas arriba, luego guardamos esto en el filename.
        """
        filename = f"{cls.__name__}.json"
        new_list = []

        if list_objs is not None or len(list_objs) > 0:
            for object in list_objs:
                new_list += [object.to_dictionary()]

        json_list_dict = Base.to_json_string(new_list)

        with open(filename, "w", encoding="UTF-8") as f:
            f.write(json_list_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        Create a static method that returns the list of the JSON string
        representation "json_string".
        Aca se pasa de un json_string a una lista de python.
        """
        import json

        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This is a class method that returns an instance (object) with all
        attributes already set.
        Inside "**dictionary" are the keys and values to set to the new
        instance.
        We are going to use the method "update" that was created in the other
        classes (Rectangle and Square).
        """
        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        real_values = dummy
        return real_values

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances.
        - The filename must be: <Class name>.json - example: Rectangle.json
        - If the file doesn’t exist, return an empty list
        - Otherwise, return a list of instances - the type of these instances
        depends on cls (current class using this method).
        - You must use the from_json_string and create methods (implemented
        previously).
        """
        filename = f"{cls.__name__}.json"
        instances_list = []

        try:
            with open(filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_of_dicts = cls.from_json_string(raw_json)
            for instance in list_of_dicts:
                instances_list.append(cls.create(**instance))
        except Exception:
            pass
        return instances_list
