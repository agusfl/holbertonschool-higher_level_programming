#!/usr/bin/python3
"""
Function that appends a string at the end of a text file (UTF8) and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """Function to append some text"""
    with open(filename, 'a', encoding="utf8") as f:
        append_data = f.write(text)
        return append_data
