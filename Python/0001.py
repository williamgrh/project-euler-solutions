#
# 0001 - Multiples of 3 and 5
#
# https://projecteuler.net/problem=1
# https://github.com/williamgrh/ProjectEulerSolutions
#


def compute(max):
    ans = sum(x for x in range(max) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)

if __name__ == "__main__":
    print compute(1000)
