#!/usr/bin/python3
"""
Function that replaces or adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    new_key_value = {key: value}
    a_dictionary.update(new_key_value)
    return a_dictionary
