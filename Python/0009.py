#
# 0009 - Special Pythagorean triplet
#
# https://projecteuler.net/problem=9
# https://github.com/williamgrh/ProjectEulerSolutions
#


def compute():
    for c in range(1000):
        for b in range(c):
            for a in range(b):
                if a + b + c == 1000 and check_triplet(a, b, c):
                    return (a * b * c)


def check_triplet(a, b, c):
    if (a**2 + b**2 == c**2):
        return True
    else:
        return False


if __name__ == "__main__":
    print (str(compute()))
