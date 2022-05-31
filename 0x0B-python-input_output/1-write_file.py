#!/usr/bin/python3
"""
Function that writes a string to a text file (with UTD8) and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
