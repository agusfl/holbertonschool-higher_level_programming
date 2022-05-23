#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for testing function max_integer from 6-max_integer.py
    """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([[9, 1], [5, 6], [4, 8]]), [9, 1])

    def test_none(self):
        self.assertIsNone(max_integer([None]))
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)

    def test_signed_numbers(self):
        self.assertEqual(max_integer([5, -6, -7, 8]), 8)
        self.assertEqual(max_integer([5, -6.8, -7.5, 8]), 8)

    def test_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'f', 'z']), 'z')
        self.assertEqual(max_integer("468"), '8')
        self.assertEqual(max_integer(["Hi", "Xavier"]), "Xavier")

    def test_assertRaise(self):
        with self.assertRaises(TypeError):
            max_integer(5)
        with self.assertRaises(TypeError):
            max_integer({1, 5, 6})


if __name__ == "__main__":
    unittest.main()
