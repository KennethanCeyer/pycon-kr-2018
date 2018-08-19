import unittest
from main import sum

class TestComplexFunctions(unittest.TestCase):
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
