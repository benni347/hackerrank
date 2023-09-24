def sum_mul(n, m):
    #  Find the sum of all multiples of n below m.
    x = n
    y = n
    if n <= 0 or m <= 0:
        return "INVALID"
    else:
        while x < m:
            x += n
            y += x
            print(x)


sum_mul(2, 9)
