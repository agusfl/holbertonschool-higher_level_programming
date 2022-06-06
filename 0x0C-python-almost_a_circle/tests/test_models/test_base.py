#!/usr/bin/python3
"""
Test suite for Base class --> Unittest
--> run with python3 -m unittest discover tests
or --> run with python3 -m unittest tests/test_models/test_base.py
- All your test files and folders should start with test_
"""
from operator import le
from re import S
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    """
    Test suite for Base class.
    """
    def test_multiple_ids(self):
        """
        Test if id is correct after multiple instances are created.
        """

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_id_given(self):
        """
        Test ids match when given
        """
        self.assertTrue(Base(19), self.id == 19)
        self.assertTrue(Base(-5), self.id == -5)
        self.assertTrue(Base(1125), self.id == 1125)

    def test_empty_arg(self):
        """
        Test when no arguments are passed
        """
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)

    def test_invalid_args(self):
        """
        Test too many args given throws error
        """
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """ Test if the to_json_string method works
        """
        json_string = Base.to_json_string([{'value': 1}])
        json_string_two = Base.to_json_string([{'value': 1}, {'value2': 2}])

        self.assertEqual(json_string, '[{"value": 1}]')
        self.assertEqual(json_string_two, '[{"value": 1}, {"value2": 2}]')

    def test_to_json_string_none(self):
        """
        Test when None is passed to: to_json_string
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_to_json_string_empty_list(self):
        """
        Test when: to_json_string is passed as an empty list
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_save_to_file_one(self):
        """
        Test if save_to_file method works
        """
        r1 = Rectangle(10, 7, 2, 8, 50)
        s1 = Square(8, 2, 3, 50)
        r1_dictionary = [{"y": 8, "x": 2, "id": 50, "width": 10, "height": 7}]
        s1_dictionary = [{"id": 50, "y": 3, "x": 2, "size": 8}]

        Rectangle.save_to_file([r1])
        Square.save_to_file([s1])

        with open("Rectangle.json", "r") as file1:
            r1_file_dict = file1.read()

        with open("Square.json", "r") as file2:
            s1_file_dict = file2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        # Esto es para que no se quede guardado el archivo que se crea.
        os.remove("./Square.json")

    def test_save_to_file_empty_list(self):
        """
        Test if save_to_file method can handle empty lists.
        """
        r1_dictionary = []
        s1_dictionary = []
        Rectangle.save_to_file([])
        Square.save_to_file([])

        with open("Rectangle.json", "r") as f1:
            r1_file_dict = f1.read()

        with open("Square.json", "r") as f2:
            s1_file_dict = f2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        os.remove("./Square.json")

    def test_save_to_file_none(self):
        """
        Test if save_to_file method can handle None.
        """
        r1_dictionary = []
        s1_dictionary = []
        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        with open("Rectangle.json", "r") as file1:
            r1_file_dict = file1.read()

        with open("Square.json", "r") as file2:
            s1_file_dict = file2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        os.remove("./Square.json")

    def test_from_json_string_Rectangle(self):
        """
        Test if from_json_string method works on Rectangle class.
        """

        list_input = [{'id': 2, 'width': 10, 'height': 4},
                      {'id': 4, 'width': 1, 'height': 7}]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        expected = [{"height": 4, "width": 10, "id": 2},
                    {"height": 7, "width": 1, "id": 4}]

        self.assertEqual(list_output, expected)

    def test_from_json_string_Square(self):
        """ Test if from_json_string method works on Square
        """

        list_input = [{'id': 2, 'size': 3},
                      {'id': 4, 'size': 1}]

        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        expected = [{'id': 2, 'size': 3},
                    {'id': 4, 'size': 1}]

        self.assertEqual(list_output, expected)
