#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class, otherwise
return False.
"""


def inherits_from(obj, a_class):
    """
    Function to know if the obj is a class or inherited class of a_class.
    """
    if issubclass(type(obj), a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
