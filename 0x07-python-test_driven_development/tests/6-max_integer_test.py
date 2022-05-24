#!/usr/bin/python
"""Tests for task 6-max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests of function max_integer"""
    def test_normal(self):
        """Tests normal"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_none(self):
        """Tests empty"""
        self.assertEqual(max_integer(), None)

    def test_negative(self):
        """Tests negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed(self):
        """Tests negative and positive numbers"""
        self.assertEqual(max_integer([1, -2, -3, 4, 5]), 5)

    def test_not_int(self):
        """Tests input that's not int"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_float(self):
        """Tests with float"""
        self.assertEqual(max_integer([1, 2, 3.3]), 3.3)

if __name__ == "__main__":
    unittest.main()
