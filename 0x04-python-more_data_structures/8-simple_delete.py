#!/usr/bin/python3
"""
Function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary
