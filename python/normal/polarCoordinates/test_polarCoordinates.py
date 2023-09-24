import unittest
from polarCoordinates import (
    convert_to_polar,
)  # Adjust this import according to your actual project structure
import math


class TestPolarCoordinates(unittest.TestCase):
    def test_origin(self):
        r, theta = convert_to_polar(complex(0, 0))
        self.assertEqual(r, 0)
        self.assertEqual(theta, 0)

    def test_positive_real_axis(self):
        r, theta = convert_to_polar(complex(1, 0))
        self.assertEqual(r, 1)
        self.assertEqual(theta, 0)

    def test_positive_imaginary_axis(self):
        r, theta = convert_to_polar(complex(0, 1))
        self.assertEqual(r, 1)
        self.assertEqual(theta, math.pi / 2)

    def test_negative_real_axis(self):
        r, theta = convert_to_polar(complex(-1, 0))
        self.assertEqual(r, 1)
        self.assertEqual(theta, math.pi)

    def test_negative_imaginary_axis(self):
        r, theta = convert_to_polar(complex(0, -1))
        self.assertEqual(r, 1)
        self.assertEqual(theta, -math.pi / 2)

    def test_arbitrary_point(self):
        r, theta = convert_to_polar(complex(3, 4))
        self.assertEqual(r, 5)
        self.assertAlmostEqual(theta, 0.927, places=3)


if __name__ == "__main__":
    unittest.main()
