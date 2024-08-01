#!/bin/python3

import re


def decode_matrix(matrix):
    transposed = ["".join(row) for row in zip(*matrix)]
    joined = "".join(transposed)
    return re.sub(r"(?<=\w)[^\w]+(?=\w)", " ", joined)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = [input() for _ in range(n)]
result = decode_matrix(matrix)
print(result)
