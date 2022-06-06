#!/usr/bin/python3
"""
Test suite for Rectangle class --> Unittest
--> run with python3 -m unittest discover tests
or --> run with python3 -m unittest tests/test_models/test_rectangle.py
- All your test files and folders should start with test_
"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):
    """
    Tests the rectangle class
    """

    def test_id(self):
        """
        Tests the correct output of the id of the class Rectangle
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(1, 2, 3, 4, 55)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 55)

    def test_width(self):
        """
        Test setting attribute width
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.width, 3)

    def test_height(self):
        """
        Test setting attribute height
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 4)

    def test_no_arguments(self):
        """
        Test when attributes width and height aren't passed
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_with_width_and_height(self):
        """
        Test when attributes width and height are passed
        """
        Base._Base__nb_objects = 0

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
