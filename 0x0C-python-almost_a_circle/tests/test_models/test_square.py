#!/usr/bin/python3
"""
Test suite for Square class --> Unittest
--> run with python3 -m unittest discover tests
or --> run with python3 -m unittest tests/test_models/test_square.py
- All your test files and folders should start with test_
"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Square(unittest.TestCase):
    """
    Tests the Square class
    """

    def test_id(self):
        """
        Tests the id of the Square class
        """
        Base._Base__nb_objects = 0
        s1 = Square(10, 2)
        s3 = Square(1, 2, 3, 4)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s3.id, 4)

    def test_size(self):
        """
        Test setting attribute: size
        """
        s1 = Square(1, 2)
        s2 = Square(2, 3)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.size, 2)

    def test_square__with_no_arguments(self):
        """
        Test when no arguements are being passed
        """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_default_attributes(self):
        """
        Test if default attributes are set when no attributes are given
        """
        s2 = Square(1)
        self.assertTrue(s2.size == 1)
        self.assertTrue(s2.x == 0)
        self.assertTrue(s2.y == 0)
        self.assertTrue(s2.id is not None)

    def test_all_attr_given(self):
        """
        Test when all attributes are passed
        """
        s1 = Square(1, 2, 3, 4)
        self.assertTrue(s1.size == 1)
        self.assertTrue(s1.x == 2)
        self.assertTrue(s1.y == 3)
        self.assertTrue(s1.id == 4)

    def test_attributes_validation(self):
        """
        Test if attributes are validated before setting them
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
            Square([1, 2, 3])
            Square({1, "set", 3})
            Square({"dict": 1})
            Square(None)
            Square(("tuple", 1))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(1).size(-1)

    def test_too_many_args(self):
        """
        Test if too many args given throws an error
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7, 8)

    def test_too_little_args(self):
        """
        Test if too little args given throws an error
        """
        with self.assertRaises(TypeError):
            Square()

    def test_None_args(self):
        """
        Test if None args is given throws an error
        """
        with self.assertRaises(TypeError):
            Square(None)

    def test_area(self):
        """
        Test inherited method: area
        """
        self.assertEqual(Square(2).area(), 4)
        self.assertEqual(Square(4).area(), 16)

    def test_print(self):
        """
        Test inherited method: __str__
        """
        sq = Square(1, 2, 3, 4)
        sq.size = 5
        self.assertEqual(str(sq), '[Square] (4) 2/3 - 5')

    def test_update(self):
        """
        Test method: update --> *args and **kwargs
        """
        sq = Square(1, 2, 3, 4)
        sq.update(1, 1, 1, 1)
        self.assertEqual(str(sq), '[Square] (1) 1/1 - 1')
        sq.update()
        sq.update(2)
        self.assertEqual(str(sq), '[Square] (2) 1/1 - 1')
        sq.update(3, 4)
        self.assertEqual(str(sq), '[Square] (3) 1/1 - 4')
        sq.update(5, 6, 7, 8)
        self.assertEqual(str(sq), '[Square] (5) 7/8 - 6')

        sq.update(id=9, size=10)
        self.assertEqual(str(sq), '[Square] (9) 7/8 - 10')

    def test_to_dictionary(self):
        """
        Test method: to_dictionary
        """
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        s2 = Square(1, 2)
        s2.update(**sdic)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')
