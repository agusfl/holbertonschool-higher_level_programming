#!/usr/bin/python3
"""
Module: 3-say_my_name defines a function that print a phrase.
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print first and last name passed as arguments.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
