#!/usr/bin/python3
"""
Function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for i in range(x):
        try:
            print(f"{my_list[i]:d}", end="")
            cont += 1
        except (TypeError, ValueError):
            continue
    print("")
    return cont
