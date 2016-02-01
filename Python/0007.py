#
# 0007 - 10001st prime
#
# https://projecteuler.net/problem=7
# https://github.com/williamgrh/ProjectEulerSolutions
#

import eulerlib

def compute():
    ans, count = 1, 0
    while count < 10001:
        ans += 1
        if eulerlib.is_prime(ans):
            count += 1
    return ans


if __name__ == "__main__":
    print ( str( compute() ) )