#
# 0006 - Sum square difference
#
# https://projecteuler.net/problem=6
# https://github.com/williamgrh/ProjectEulerSolutions
#


def compute():
    x, y = 0, 0
    for i in range(1, 101):
        x += i**2
    y = sum(range(1, 101))**2
    return y - x


if __name__ == "__main__":
    print (str(compute()))
