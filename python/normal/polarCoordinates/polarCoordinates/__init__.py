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
TODO: Your problem description here.

:author: Cedric Skwar <cdrc@5y5.one>
:license: GNU General Public License v3 or later (GPLv3+)
:problem_url: https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
import cmath


def convert_to_polar(z: complex):
    # Calculate the magnitude (r) and angle (theta) in radians
    r = abs(z)
    theta = cmath.phase(z)
    return r, theta


if __name__ == "__main__":
    z = complex(input())
    r, theta = convert_to_polar(z)
    print(f"{r}\n{theta}")
