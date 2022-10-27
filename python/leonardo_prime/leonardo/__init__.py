#!/usr/bin/env python3
"""
:URL:	https://www.hackerrank.com/challenges/leonardo-and-prime/problem
"""

def primeCounter(n):
    if n == 1:
        return 0


if __name__ == "__main":
    t = int(input().strip())
    for tc in rang(t):
        n = int(input().strip())
        result = primeCounter(n)

