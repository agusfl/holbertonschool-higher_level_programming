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

    def test_default_attributes(self):
        """
        Test if default attributes are set when no attributes are given
        """
        r2 = Rectangle(1, 2)
        self.assertTrue(r2.width == 1)
        self.assertTrue(r2.height == 2)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_all_attr_given(self):
        """
        Test when all attributes are passed
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertTrue(r1.width == 1)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r1.x == 3)
        self.assertTrue(r1.y == 4)
        self.assertTrue(r1.id == 5)

    def test_attributes_validation(self):
        """
        Test if attributes are validated before setting them
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(["list", "as_string"], "second_parameter_required")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2, 2}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, ("tuple", 1), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -10, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -255, 1)

    def test_too_many_args(self):
        """
        Test if too many args given throws an error
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7, 8)

    def test_too_little_args(self):
        """
        Test if too little args given throws an error
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_None_args(self):
        """
        Test if None args is given throws an error
        """
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_private_attr_access(self):
        """
        Test if private attributes are not accessible, as they should
        """
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_area(self):
        """
        Test inherited method: area
        """
        self.assertEqual(Rectangle(2, 2).area(), 4)
        self.assertEqual(Rectangle(4, 4).area(), 16)

    def test_print(self):
        """
        Test inherited method: __str__
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    def test_display(self):
        """
        Test inherited method: display
        """
        import sys
        import io

        display = "##\n##\n##\n"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3)
        r1.display()
        self.assertEqual(capturedOutput.getvalue(), display)

        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        """
        Test method: to_dictionary
        """
        dic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(dic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**dic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
