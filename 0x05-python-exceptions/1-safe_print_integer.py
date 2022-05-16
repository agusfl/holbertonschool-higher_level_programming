#!/usr/bin/python3
"""
Function that prints an integer with "{:d}".format().
"""


def safe_print_integer(value):
    try:
        print(f"{value:d}")
        return True
    except (TypeError, ValueError):
        return False
