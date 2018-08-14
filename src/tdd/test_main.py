import unittest

from main import calc


class TestTdd(unittest.TestCase):
    def test_calc(self):
        given = (1, 2, 3, 4, 5)
        target = calc(given)
        expected = 15
        self.assertEqual(target, expected)

    def test_calc_with_various_odd(self):
        given = (1, 3, 5, 6, 7)
        target = calc(given)
        expected = 20
        self.assertEqual(target, expected)

    def test_calc_with_empty(self):
        given = ()
        target = calc(given)
        expected = 0
        self.assertEqual(target, expected)

    def test_calc_with_none(self):
        given = None
        with self.assertRaises(TypeError):
            calc(given)
