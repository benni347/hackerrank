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
:problem_url: https://www.hackerrank.com/challenges/python-time-delta/problem
"""

import datetime
import os


def time_delta(time_1: str, time_2: str):
    time_delta = int(
        datetime.timedelta(
            seconds=datetime.datetime.strptime(
                time_2, "%a %d %b %Y %H:%M:%S %z"
            ).timestamp()
            - datetime.datetime.strptime(time_1, "%a %d %b %Y %H:%M:%S %z").timestamp()
        ).total_seconds()
    )
    if time_delta < 0:
        time_delta *= -1
    return str(time_delta)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + "\n")

    fptr.close()
