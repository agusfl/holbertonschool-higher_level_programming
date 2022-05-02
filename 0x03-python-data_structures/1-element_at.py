#!/usr/bin/python3
"""
Function that retrieves an element from a list line in C.
"""


def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    else:
        for i in my_list:
            if i == idx:
                return my_list[idx]
