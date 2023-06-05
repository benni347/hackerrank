#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/write-a-function/problem
# Author:  benni347@github.com

def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
       leap = True
    return leap

year = int(input())
print(is_leap(year))
