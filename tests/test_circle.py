import unittest

from simple_shape_lib import Circle


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(circle.calculate_area(), 78.53981633974483)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_invalid_circle_2(self):
        with self.assertRaises(ValueError):
            Circle("0")
