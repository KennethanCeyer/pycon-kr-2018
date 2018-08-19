import unittest
import math
import numpy as np
from main import sum, get_version


def is_array_numeric(array):
    return np.asarray(array).dtype.kind.lower() in ('b', 'u', 'i', 'f', 'c')


class TestBasicFunctions(unittest.TestCase):
    def test_sum(self):
        target = sum(3, 4)
        expected = 7
        self.assertEqual(target, expected)

    def test_sum_with_negative_args(self):
        target = sum(-1, 5)
        expected = 4
        self.assertEqual(target, expected)

    def test_sum_with_none(self):
        with self.assertRaises(TypeError):
            sum(None, 2)

    def test_get_version(self):
        target = get_version()
        items = target.split('.')
        expected_number_item = 3

        self.assertEqual(len(items), expected_number_item)
        self.assertTrue(is_array_numeric(items))
