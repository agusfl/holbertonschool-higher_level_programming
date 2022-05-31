#!/usr/bin/python3
"""
Function that reads a text file (with UTF8 encoding) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function to read a file and print it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
