#!/usr/bin/python3

"""Module for Base unit tests."""
import unittest
import pep8

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """test the Base class."""

    def test_init(self):
         """tests."""
         b1 = Base()
         self.assertEqual(b1.id, 1)

         b2 = Base()
         self.assertEqual(b2.id, 2)

         b3 = Base()
         self.assertEqual(b3.id, 3)

         b4 = Base(12)
         self.assertEqual(b4.id, 12)

         b5 = Base()
         self.assertEqual(b5.id, 4)

    def test_json(self):
        """base json tests."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertAlmostEqual(print(dictionary), print(d))
        self.assertAlmostEqual(print(type(dictionary)),print("<class 'dict'>"))
        d = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertAlmostEqual(print(json_dictionary), print(d))
        self.assertAlmostEqual(print(type(json_dictionary)),print("<class 'str'>"))

    def test_json_to_file(self):
        """update tests."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        d = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        with open("Rectangle.json", "r") as file:
            self.assertEqual(print(file.read()), print(d))

    def test_from_json_string(self):
        """tests"""
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]"
        self.assertEqual(print(l), print("[{}] {}".format(type(list_output), list_output)))
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(print("[]"), print("[{}] {}".format(type(list_output), list_output)))


