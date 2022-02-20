#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    idx = 0
    rs = len(s)
    a = []
    for w in s:
        if len(w) > 0:
            w = w[0].upper() + w[1:]
        s[idx] = w
        idx += 1
    s = " ".join(s)
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = str(input())
    s = "hello   world  lol"
#    s = "hello world lol"

    # solve("john doe")
    result = solve(s)

    fptr.write(result + '\n')
    fptr.close()
