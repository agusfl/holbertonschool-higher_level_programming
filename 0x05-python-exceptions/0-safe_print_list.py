#!/usr/bin/python3
"""
Function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        while cont < x:
            print(f"{my_list[cont]}", end="")
            cont += 1
    except IndexError:
        pass
    print("")
    return cont
