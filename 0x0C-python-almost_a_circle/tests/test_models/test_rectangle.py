#!/usr/bin/python3

"""
    tests for file rectangle.py
"""


import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class for testing Rectangle class' methods
    """
    def test_Normal_values(self):
        """
        Normal values just for width and height
        """
        R1 = Rectangle(1, 2)
        R2 = Rectangle(1, 2, 3)
        R3 = Rectangle(1, 2, 3, 4)
        R4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 0, 0, 1])
        self.assertEqual([R2.width, R2.height, R2.x, R2.y, R2.id],
                         [1, 2, 3,  0, 2])
        self.assertEqual([R3.width, R3.height, R3.x, R3.y, R3.id],
                         [1, 2, 3, 4, 3])
        self.assertEqual([R4.width, R4.height, R4.x, R4.y, R4.id],
                         [1, 2, 3, 4, 5])

    def test_wrong_inputted_values(self):
        """
        Test for negative and zero values
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            R = Rectangle(-4, -5)
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """
        Different types for inputted arguments
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            R = Rectangle(-4, -5)
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            R = Rectangle('width', 'height')
        with self.assertRaises(TypeError):
            R = Rectangle(2.4, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(True, False)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, True, False)
        with self.assertRaises(TypeError):
            R = Rectangle([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            R = Rectangle({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """
        Test for area method
        """
        R = Rectangle(10, 10)
        self.assertEqual(R.area(), 100)
        with self.assertRaises(TypeError):
            A = R.area(1)

    def test_str(self):
        """
        Test for __str__ method
        """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(R))
