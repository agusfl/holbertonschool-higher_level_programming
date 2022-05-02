#!/usr/bin/python3
"""
Function that prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list is not None:
        for i in my_list:
            print(f"{i:d}")
