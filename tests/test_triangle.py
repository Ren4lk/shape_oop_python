import unittest

from simple_shape_lib import Triangle


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_triangle_not_right(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 4)

    def test_invalid_triangle_2(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, 3, 1)

    def test_invalid_triangle_3(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, "5")
