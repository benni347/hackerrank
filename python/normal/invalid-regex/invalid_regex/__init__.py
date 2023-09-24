#!/usr/bin/env python3
"""
:URL:	https://www.hackerrank.com/challenges/incorrect-regex/
"""
import re


def check(pattern):
    """
    This will check if a given regex pattern is valid.
    :pattern: Should be a regex string.
    :return: True if regex is valid and false if it isn't valid.
    """
    try:
        re.compile(pattern)
    except re.error:
        return "False"
    else:
        return "True"

if __name__ == "__main__":
    t = int(input().strip())
    for tc in range(t):
        print(check(input()))

