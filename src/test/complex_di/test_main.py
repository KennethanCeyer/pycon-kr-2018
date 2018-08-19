import unittest
from main import sum


def _get_year(_):
    return 2018


class TestComplexFunctions(unittest.TestCase):
    def test_sum(self):
        target = sum(_get_year, None, 3, 4)
        expected = 7
        self.assertEqual(target, expected)

    def test_sum_with_negative_args(self):
        target = sum(_get_year, None, -1, 5)
        expected = 4
        self.assertEqual(target, expected)

    def test_sum_with_none(self):
        with self.assertRaises(TypeError):
            sum(_get_year, None, None, 2)
