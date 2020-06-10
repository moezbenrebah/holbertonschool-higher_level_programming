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
