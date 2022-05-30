#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Available list of attributes and methods of an object
    """
    return dir(obj)
