import unittest
from invalid_regex import check



class MyTestCase(unittest.TestCase):
    def test_valid(self):
        test_data = ((r".*\+", "True"), (r".*?", "True"), (r".*?", "True"))

        for variant, data in enumerate(test_data, start=1):
            regex_str, expected = data
            with self.subTest(f'variation #{variant}',  neutrons_emitted=regex_str, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = check(regex_str)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'regex_str={regex_str}')
                self.assertEqual(actual_result, expected, failure_message)

    def test_invalid(self):
        test_data = ((r"*", "False"), (r"+*", "False"), (r".+*", "False"))

        for variant, data in enumerate(test_data, start=1):
            regex_str, expected = data
            with self.subTest(f'variation #{variant}',  neutrons_emitted=regex_str, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = check(regex_str)
                failure_message = (f'Expected {expected} but returned {actual_result} '
                                   f'regex_str={regex_str}')
                self.assertEqual(actual_result, expected, failure_message)


if __name__ == '__main__':
    unittest.main()
