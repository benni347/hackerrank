import unittest
from unittest.mock import patch
from io import StringIO

# Read the content of postal/__init__.py into a string
with open("postal/__init__.py", "r") as f:
    original_code = f.read()


class TestPostalCodeValidation(unittest.TestCase):
    def run_code_with_mock_input(self, mock_input):
        with patch("builtins.input", return_value=mock_input):
            with patch("sys.stdout", new=StringIO()) as mock_output:
                # Executing the original code
                exec(original_code)
                return mock_output.getvalue().strip()

    def test_invalid_postal_code(self):
        output = self.run_code_with_mock_input("110000")
        self.assertEqual(output, "False")

    def test_invalid_postal_code_length(self):
        output = self.run_code_with_mock_input("11000")
        self.assertEqual(output, "False")

    def test_invalid_starting_digit(self):
        output = self.run_code_with_mock_input("010000")
        self.assertEqual(output, "False")

    def test_valid_alternating_repetitive_digits(self):
        output = self.run_code_with_mock_input("110011")
        self.assertEqual(output, "True")

    def test_another_valid_postal_code(self):
        output = self.run_code_with_mock_input("123456")
        self.assertEqual(output, "True")

    def test_another_invalid_postal_code(self):
        output = self.run_code_with_mock_input("111111")
        self.assertEqual(output, "False")


if __name__ == "__main__":
    unittest.main()
