#!/usr/bin/python3
"""
Function that returns True if the object is an instance of the specified class
or if the object is an instance of a class that inherited from
otherwise return False.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to know if an object is an instance of a specified class
    or if the obj is an instance of a class that inherited from.
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
