#!/usr/bin/python3
"""
Create a class Student that defines a student with: first_name, last_name
and age.
Has a public instance to_json that retrieves a dictionary representation of
a student.
"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Hasta aca es el mismo codigo que en el ejercicio anterior.
    def to_json(self, attrs=None):
        """function that retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for attribute in attrs: # se refiere a las keys (del dict)
                if attribute in self.__dict__.keys(): # se refiere a las keys (del dict)
                    dictionary[attribute] = self.__dict__[attribute] # se refiere a los valores (del dict)
            return dictionary

# Lo que hacemos aca es agregar el argumento "attrs" que viene de atributes, primero que nada ponemos la condicion
# de letra para evaluar el caso de que "attrs" este vacio (None) como se puede ver en el archivo 10-main.py que el
# primer j_student_1 que llaman --> que seria la llamada al metodo que creamos "to_json" en esta clase Student para
# el objeto que crean en el main "student_1", como se pueden ver no pasan ningun argumento ahi entonces como nos indica
# al letra si no se pasa ningun argumento se tiene que retornar el diccionario con todas las key-value que tenga dicho
# objeto.
# Si solo se pasa algunos atributos como ser en el j_student_2 que solo se pasan los atributos: first_name y age - se
# tienen que imprimir solo los atributos que se pasaron. Esto lo hacemos en el else, donde creamos un diccionario
# nuevo para ir guardando lo que queremos retornar para que en el main lo puedan imprimir. Hacemos un for para que
# recorra cada atributo (attribute) dentro de los "attrs" que se pasen como argumento y si "attribute" esta dentro
# de las keys en el __dict__ (el dict tiene todos los atributos del objeto) vamos a guardar dentro del diccionario
# que creamos ("dictionary") el atributo correspondiente con su key, por lo tanto vamos a retornar solo lo que
# estuviera en el __dict__ y que guardamos en nuestro "dictionary".
# "attribute" solo hace referencia al nombre de la "key", como ser: first_name, last_name, age y al
# poner: dictionary[attribute] se hace referencia al valor del atributo, como ser: John, Doe, 23.
