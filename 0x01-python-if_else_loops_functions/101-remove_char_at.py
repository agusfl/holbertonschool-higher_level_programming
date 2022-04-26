#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str_copy = str[:n] + str[(n+1):]
    else:
        str_copy = str
    return str_copy
