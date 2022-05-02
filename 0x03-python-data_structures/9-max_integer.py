#!/usr/bin/python3
"""
Function that finds the biggest integer of a list.
"""


def max_integer(my_list=[]):
    if my_list is None:
        return None
    max_number = 0
    for i in my_list:
        if i > max_number:
            max_number = i
    return max_number
