#!/usr/bin/env python3

import math


def prime(n):
    i = 3
    prime_numbers = [2, 3]
    if(0 < n < 3):
        print(n)
    elif(n > 2):
        while (True):
            i += 1
            status = True
            for j in range(2, int(i/2)+1):
                if(i % j == 0):
                    status = False
                    break
            if(status == True):
                prime_numbers.append(i)
            if(len(prime_numbers) == n):
                break
        print(prime_numbers[n-1])


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        prime(n)
