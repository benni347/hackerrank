#!/bin/python3

import os


def solve(s):
    s = s.split(" ")
    idx = 0
    for w in s:
        if len(w) > 0:
            w = w[0].upper() + w[1:]
        s[idx] = w
        idx += 1
    s = " ".join(s)
    return s


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = "hello   world  lol"
    result = solve(s)

    fptr.write(result + "\n")
    fptr.close()
