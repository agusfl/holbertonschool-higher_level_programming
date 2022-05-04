#!/usr/bin/python3
"""
Function that replaces all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    else:
        new_list = []
        for i in my_list:
            if i == search:
                new_list.append(replace)
            else:
                new_list.append(i)
        return new_list
