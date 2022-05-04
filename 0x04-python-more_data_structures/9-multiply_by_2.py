#!/usr/bin/python3
"""
Function that returns a new dictionary with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        mul_by_2 = value * 2
        temp_dict = {key: mul_by_2}
        new_dictionary.update(temp_dict)
    return new_dictionary
