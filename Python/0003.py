#
# 0003 - Largest prime factor
#
# https://projecteuler.net/problem=3
# https://github.com/williamgrh/ProjectEulerSolutions
#

import eulerlib


def compute():
    n = 600851475143
    f = 0
    for i in range(2, eulerlib.sqrt(n) + 1):
        if eulerlib.is_prime(i) and n % i == 0:
            f = i
    return f


if __name__ == "__main__":
    print ( str( compute() ) )