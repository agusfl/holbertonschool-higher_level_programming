#!/usr/bin/python3
"""
Create a class Student that defines a student with: first_name, last_name
and age.
"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that retrieves a dictionary representation of a Student"""
        return self.__dict__
