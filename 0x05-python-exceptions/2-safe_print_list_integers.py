#!/usr/bin/python3
"""
Function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    for cont in range(x):
        try:
            print(f"{my_list[cont]:d}", end="")
            cont += 1
        except (TypeError, ValueError):
            cont -= 1
            continue
    print("")
    return cont
