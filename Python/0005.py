#
# 0005 - Smallest multiple
#
# https://projecteuler.net/problem=5
# http://git.wgrh.io/will/project-euler-solutions
#

import eulerlib


def compute():
    ans = 1
    for i in range(1, 21):
        ans *= i // eulerlib.gcd(i, ans)
    return ans


if __name__ == "__main__":
    print (str(compute()))
