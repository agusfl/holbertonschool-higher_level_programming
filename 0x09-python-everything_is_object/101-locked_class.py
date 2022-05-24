#!/usr/bin/python3
"""
Class LockedClass that has no class or object attributes that prevents the
user from dynamically creating new instances attributes except if the new
instance attribute is called: first_name
"""


class LockedClass:
    """
    Implementation of LocjedClass, using __slot__
    Documentation: https://stackoverflow.com/questions/3603502/prevent-creating
    -new-attributes-outside-init
    """
    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "John"
