#
# Shared code for Project Euler problems
#
# https://projecteuler.net/
# https://github.com/williamgrh/ProjectEulerSolutions
#

import sys
if sys.version_info.major == 2:
    range = xrange


# Returns the greatest common denominator of the given non-negative integers
def gcd(x, y):
    assert x >= 0 and y >= 0
    while y != 0:
        x, y = y, x % y
    return x


# Given integer x, returns the integer floor(sqrt(x))
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y


# Tests whether the given integer is prime
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, sqrt(x)+1, 2):
            if x % i == 0:
                return False
        return True


# Returns the factorial of the given non-negative integer
def factorial(x):
    assert x >= 0
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result