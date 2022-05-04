#!/usr/bin/python3
"""
Function that returns a set of all elements present in only one set.
En la documentacion oficial de python se puede ver que ^ se usa para ver los
elementos que se encuentran tanto en el set 1 o el set 2 pero no en los dos.
"""


def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
