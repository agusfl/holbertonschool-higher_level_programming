#!/usr/bin/python3
import numpy as np
"""
Module 101-lazy_matrix_mul
This is a module for multiply two matrices using numpy module
To install numpy on ubuntu use: pip install numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Using numpy module to multiply 2 matrices.
    """
    return np.dot(m_a, m_b)
