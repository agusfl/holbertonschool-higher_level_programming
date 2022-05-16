#!/usr/bin/python3
import sys
"""
Function that prints an integer.
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (Exception) as errors:
        sys.stderr.write("Exception: {}\n".format(errors))
        return False
