#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance of the
specified class, otherwise return False.
"""


def is_same_class(obj, a_class):
    """
    Function to know if an object is an instance of a specified class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
