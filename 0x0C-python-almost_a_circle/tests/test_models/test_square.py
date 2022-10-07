#!/usr/bin/python3

""" tests for class square"""


import sys
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    class for testing Square class' methods
    """

    def test_Normal_values(self):
        """
        Normal values just for width and height
        """
        S1 = Square(1, 2)
        S2 = Square(1, 2, 3)
        S3 = Square(1, 2, 3, 4)
        self.assertEqual([S1.size, S1.x, S1.y, S1.id],
                         [1, 2, 0, 1])
        self.assertEqual([S2.size, S1.x, S1.y, S2.id],
                         [1, 2, 0, 2])
        self.assertEqual([S3.size, S1.x, S1.y, S3.id],
                         [1, 2, 0, 4])

    def test_wrong_inputted_values(self):
        """
        Test for negative and zero values
        """
        with self.assertRaises(ValueError):
            S = Square(0, 0)
        with self.assertRaises(ValueError):
            S = Square(-4, -5)
        with self.assertRaises(ValueError):
            S = Square(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """
        Different types for inputted arguments
        """
        with self.assertRaises(TypeError):
            S = Square('width', 'height')
        with self.assertRaises(TypeError):
            S = Square(2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(True, False)
        with self.assertRaises(TypeError):
            S = Square(1, 2, True, False)
        with self.assertRaises(TypeError):
            S = Square([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """
        Test for area method
        """
        S = Square(10, 10)
        self.assertEqual(S.area(), 100)
        with self.assertRaises(TypeError):
            A = S.area(1)

    def test_str(self):
        """
        Test for __str__ method
        """
        S = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(S))

    def test_update_args(self):
        """
        Test for update method: args
        """
        S = Square(1, 2, 3, 4)
        S.update(6)
        self.assertEqual(6, S.id)
        S.update(6, 7)
        self.assertEqual(7, S.size)
        S.update(6, 7, 8)
        self.assertEqual(8, S.x)
        S.update(6, 7, 8, 9)
        self.assertEqual(9, S.y)

    def test_display(self):
        """
        Test display method
        """
        S = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 2)
        S = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2))

    def test_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        Sq = Square(1, 2, 3, 4)
        Sq.update(5, id=6)
        self.assertEqual([Sq.id, Sq.size, Sq.x, Sq.y], [5, 1, 2, 3])
        Sq.update(6, 7, x=9, y=10)
        self.assertEqual([Sq.id, Sq.size, Sq.x, Sq.y], [6, 7, 2, 3])
        Sq.update(width=7, id=6, height=8)
        self.assertEqual([Sq.id, Sq.size, Sq.x, Sq.y], [6, 7, 2, 3])
        Sq.update(x=40, y=5)
        self.assertEqual([Sq.id, Sq.size, Sq.x, Sq.y], [6, 7, 40, 5])

    def test_dictionary(self):
        """
        Tests for dictionary method
        """
        Sq = Square(200, 600, 100, 1000)
        Sq_dict = Sq.to_dictionary()
        self.assertEqual(Sq_dict['size'], 200)
        self.assertEqual(Sq_dict['x'], 600)
        self.assertEqual(Sq_dict['y'], 100)
        self.assertEqual(Sq_dict['id'], 1000)
