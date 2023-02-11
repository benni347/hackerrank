#!/bin/python3

import sys


def sum_even_fibonacci(num):
    sum = 0
    previous_num = 1
    current_num = 2
    while current_num <= num:
        if current_num % 2 == 0:
            sum += current_num
        current_num += previous_num
        previous_num = current_num - previous_num
    return sum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_even_fibonacci(n))
