#!/usr/bin/env python3

def triangle(q, n):
    # perfect number= 28, 6
    # 1 <= q <= 100000
    # 25 <= n <= 2 * 10**18
    sa = 7
    sb = 24
    sc = 25
    newarea = 0
    x = 1
    while x <= q:
        area = int(sa * sb * (0.5 * x))
        print("x: " + str(x))
        print("area: " + str(area))
        x += 1
    # sc <= n
    print(area)

    

if __name__ == '__main__':
    # q = int(input())
    # n = int(input())

    q = 10
    n = 25
    triangle(q, n)