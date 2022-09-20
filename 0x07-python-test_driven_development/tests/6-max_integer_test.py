#!/usr/bin/python3

"""__________________unitest for max_integer([..])__________________"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Class for testing 6-max_integer_test.py
        without arguments
    """

    def test_max_integer(self):
        """
            Normal list of positive integers
            without arguments
        """
        test_list = [1, 2, 5, 8, 6]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_integer_neg(self):
        """
            Test case for a list of positive and negative integers
            without arguments
        """
        test_list = [1, 2, 3, 8, 4, -60, -40, -11, 0]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_integer_float(self):
        """
            Test case for a list of positive and negative floating
            without arguments
        """
        test_list = [5.6, 2.3, 3.12, 8.536, 4.6, -80.0, -40.999, -12.6, 0]
        self.assertEqual(max_integer(test_list), 8.536)

    def test_max_integer_empty(self):
        """
            Test case if an empty list is passed
            without arguments
        """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_max_integer_one(self):
        """
            Test case if list just have one element
            without arguments
        """
        test_list = [2]
        self.assertEqual(max_integer(test_list), 2)

    def test_max_integer_last(self):
        """
            Test case for max integer at
            last position
        """
        test_list = [1, 2, 5, 0, 6, 9]
        self.assertEqual(max_integer(test_list), 9)

    def test_max_integer_last(self):
        """
            Test case for max integer at
            first position
        """
        test_list = [11, 2, 5, 0, 6, 9]
        self.assertEqual(max_integer(test_list), 11)

    def test_max_integer_type_tuple(self):
        """
            Test case for tuple argument
        """
        test_list = (9, 3, 1)
        self.assertEqual(max_integer(test_list), 9)

    def test_max_integer_type_int(self):
        """
            Test case for int argument
        """
        test_list = 12
        self.assertRaises(TypeError, max_integer, test_list)

    def test_max_integer_type_float(self):
        """
            Test case for float argument
        """
        test_list = 12.24
        self.assertRaises(TypeError, max_integer, test_list)

    def test_max_integer_type_dict(self):
        """
            Test case for dict argumen
        """
        test_list = {"age": 4, "weight": "75kg"}
        self.assertRaises(KeyError, max_integer, test_list)
