#!/usr/bin/python3
"""
Function that returns an object (Python data structure) represented by a JSON
string.
En este ejercicio usamos el metodo: loads() del modulo json de python.
"""
import json


def from_json_string(my_str):
    """Convert JSON object to a Python object."""
    python_obj = json.loads(my_str)
    return python_obj
