#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This should create the same folder structure for each project

:author: Cedric Skwar <cdrc@5y5.one>
:license: GNU General Public License v3 or later (GPLv3+)
"""

import os


def create_test_structure_updated(dir_name, author, problem_url):
    parent_dir = dir_name
    sub_dir = dir_name
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    full_sub_dir_path = os.path.join(parent_dir, sub_dir)
    if not os.path.exists(full_sub_dir_path):
        os.mkdir(full_sub_dir_path)

    init_path = os.path.join(full_sub_dir_path, "__init__.py")
    with open(init_path, "w") as f:
        f.write("#!/usr/bin/env python3\n\n")
        f.write(
            "# This program is free software: you can redistribute it and/or modify\n"
        )
        f.write(
            "# it under the terms of the GNU General Public License as published by\n"
        )
        f.write("# the Free Software Foundation, either version 3 of the License, or\n")
        f.write("# (at your option) any later version.\n")
        f.write("#\n")
        f.write("# This program is distributed in the hope that it will be useful,\n")
        f.write("# but WITHOUT ANY WARRANTY; without even the implied warranty of\n")
        f.write("# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n")
        f.write("# GNU General Public License for more details.\n")
        f.write("#\n")
        f.write(
            f"# You should have received a copy of the GNU General Public License\n"
        )
        f.write(
            "# along with this program.  If not, see <https://www.gnu.org/licenses/>.\n"
        )
        f.write("\n")
        f.write("'''\n")
        f.write("TODO: Your problem description here.\n")
        f.write("\n")
        f.write(f":author: {author}\n")
        f.write(":license: GNU General Public License v3 or later (GPLv3+)\n")
        f.write(f":problem_url: {problem_url}\n")
        f.write("'''\n")
        f.write("\n")
        f.write("# TODO: Your code here\n")

    # Create the test file
    test_path = os.path.join(parent_dir, f"test_{dir_name}.py")
    with open(test_path, "w") as f:
        f.write("import unittest\n")
        f.write("from unittest.mock import patch\n")
        f.write("from io import StringIO\n\n")
        f.write(f"# Read the content of {dir_name}/__init__.py into a string\n")
        f.write(f'with open("{dir_name}/__init__.py", "r") as f:\n')
        f.write("    original_code = f.read()\n\n")
        f.write(f"class Test{dir_name.capitalize()}Validation(unittest.TestCase):\n")
        f.write("    def run_code_with_mock_input(self, mock_input):\n")
        f.write("        with patch('builtins.input', return_value=mock_input):\n")
        f.write(
            "            with patch('sys.stdout', new=StringIO()) as mock_output:\n"
        )
        f.write("                # Executing the original code\n")
        f.write("                exec(original_code)\n")
        f.write("                return mock_output.getvalue().strip()\n")


dir_name = input("Please enter the name of the directory: ")
author = "Cedric Skwar <cdrc@5y5.one>"
problem_url = input("Please enter the problem URL: ")

# Call the function to create structure
create_test_structure_updated(dir_name, author, problem_url)

# Output message
print(f"Folder structure and files for {dir_name} have been created.")
