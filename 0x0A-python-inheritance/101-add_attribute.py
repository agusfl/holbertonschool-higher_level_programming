#!/usr/bin/python3
"""
Function that adds new attribute if it is possible
Use of method: setattr
"""


def add_attribute(obj, attribute, value):
    """
    Function to add attribute to object if it is possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
