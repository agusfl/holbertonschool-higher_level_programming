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

    def to_json(self, attrs=None):
        """function that retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    dictionary[attribute] = self.__dict__[attribute]
            return dictionary
