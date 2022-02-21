#!/usr/bin/env python3

import sys


def multiple(n):
    # Find the sum of all the multiples of 3 or 5 below n.
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
    return sum


if __name__ == '__main__':
    # Optimized solution.
    multiple(10**9)  # must be less than 2s. Without modules like numba.
    # t = int(input().strip())
    # for a0 in range(t):
    #     n = int(input().strip())
    #     multiple(n)
