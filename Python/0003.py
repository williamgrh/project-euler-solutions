#
# 0003 - Largest prime factor
#
# https://projecteuler.net/problem=3
# https://github.com/williamgrh/ProjectEulerSolutions
#

import eulerlib


def compute():
    n = 600851475143
    y = smallest_prime(n)
    while True:
        x = smallest_prime(n)
        if x == n:
            return y
        y = smallest_prime(n)
        x //= k
        y //= k
    
def smallest_prime(x):
    for i in range(2, eulerlib.sqrt(x) + 1):
        if i % x == 0:
            return i
    return x


if __name__ == "__main__":
    print ( str( compute() ) )