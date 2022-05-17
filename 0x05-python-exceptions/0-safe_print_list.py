#!/usr/bin/python3
"""
Function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    cont = 0
    while cont < x:
        try:
            print(f"{my_list[cont]}", end="")
        except IndexError:
            break
        cont += 1
    print("")
    return cont
