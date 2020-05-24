#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestmaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_no_args(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_beginning(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([10, 5, 6]), 10)

    def test_max_at_middle(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([10, 15, 6]), 15)

    def test_max_at_end(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([10, 5, 20]), 20)

    def test_one_negative(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-3, 5, 0]), 5)

    def test_negative_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-2, -5, -6]), -2)







if __name__ == "__main__":
    unittest.main()
