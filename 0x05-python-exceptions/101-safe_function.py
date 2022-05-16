#!/usr/bin/python3
import sys
"""
Function that executes a function safely.
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as errors:
        sys.stderr.write("Exception: {}\n".format(errors))
        return None
