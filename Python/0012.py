#
# 0012 - Highly divisible triangular number
#
# https://projecteuler.net/problem=12
# http://git.wgrh.io/will/project-euler-solutions
#

import eulerlib, itertools


def compute():
    triangle = 0
    for i in itertools.count(1):
        triangle += i
        if num_factors(triangle) >= 500:
            break
    return triangle

def num_factors(n):
    count = 0
    root = eulerlib.sqrt(n)
    for i in range(1, root + 1):
        if n % i == 0:
            count += 2
    if root**2 == n:
        count -= 1
    return count

if __name__ == "__main__":
    print str(compute())