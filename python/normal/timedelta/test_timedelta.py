# test_time_delta.py

import unittest
from timedelta import time_delta


class TestTimeDelta(unittest.TestCase):
    def test_positive_delta(self):
        self.assertEqual(
            time_delta(
                "Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"
            ),
            "25200",
        )

    def test_negative_delta(self):
        self.assertEqual(
            time_delta(
                "Sun 10 May 2015 13:54:36 -0000", "Sun 10 May 2015 13:54:36 -0700"
            ),
            "25200",
        )

    def test_zero_delta(self):
        self.assertEqual(
            time_delta(
                "Sun 10 May 2015 13:54:36 -0000", "Sun 10 May 2015 13:54:36 -0000"
            ),
            "0",
        )

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            time_delta("Sun 10 May 2015 13:54:36 -0000", "Invalid date format")


if __name__ == "__main__":
    unittest.main()
