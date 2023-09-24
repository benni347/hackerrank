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
This should validated postal codes.

Problem URL: https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true

:author: Cedric Skwar <cdrc@5y5.one>
:license: GNU General Public License v3 or later (GPLv3+)
"""

import re

regex_integer_in_range = r"\b[1-9][0-9]{5}\b"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()

print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
