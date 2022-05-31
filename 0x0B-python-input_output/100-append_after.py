#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each line containing a
specific string (see holberton example).
"""


def append_after(filename="", search_string="", new_string=""):
    """Implementation of function to insert a line of text after each line
    containing a specific string."""
    with open(filename, 'r+') as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
