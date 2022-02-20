import math

def factor(n):
    n = list(str(n))
    sum = 0
    for i in n:
        sum += math.factorial(int(i))
    return sum
    
if __name__ == '__main__':
    n = int(input())
    # n = 342
    print(factor(n))
