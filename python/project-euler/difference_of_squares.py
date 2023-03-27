import sys

def difference_of_squares(n):
    sum_of_squares = 0
    sum_nums = 0
    for i in range(1, n+1):
        sum_of_squares += i**2
        sum_nums += i
    square_of_sum = sum_nums**2
    return square_of_sum - sum_of_squares

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(difference_of_squares(n))

