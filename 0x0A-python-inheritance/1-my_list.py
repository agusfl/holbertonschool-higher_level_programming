#!/usr/bin/python3
"""
Module: 1-my_list
Has a class MyList that inherits from list
"""


class MyList(list):

    """
    Class MyList is a sub class of list.
    """
    def print_sorted(self):
        """
        Public instance method that prints the list sorted(ascending sort)
        """
        print(sorted(self))
