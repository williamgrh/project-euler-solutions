#
# 0010 - Summation of primes
#
# https://projecteuler.net/problem=10
# http://git.wgrh.io/will/project-euler-solutions
#

import eulerlib


def compute():
    ans = sum(eulerlib.list_primes(2000000))
    return ans


if __name__ == "__main__":
    print (str(compute()))
