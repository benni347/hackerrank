#!/usr/bin/env python3

import os
import re

pattern = re.compile("h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*", re.IGNORECASE)


def hackerrankInString(s):
    if pattern.search(s) is None:
        return "NO"
    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + "\n")

    fptr.close()
