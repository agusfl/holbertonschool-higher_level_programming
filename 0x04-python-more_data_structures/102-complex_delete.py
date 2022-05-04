#!/usr/bin/python3

"""
Function that deletes keys with a specific value in a dictionary.
"""


def complex_delete(a_dictionary, value):
    copy_dictionary = a_dictionary.copy()
    for key, value_iter in copy_dictionary.items():
        if value_iter == value:
            del a_dictionary[key]
    return a_dictionary
