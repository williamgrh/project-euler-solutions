#
# 0004 - Largest palindrome product
#
# https://projecteuler.net/problem=4
# http://git.wgrh.io/will/project-euler-solutions
#


def compute():
    ans, tmp = 0, 0
    for i in range(99, 1000):
        for j in range(99, 1000):
            tmp = i * j
            if (is_palindrome(tmp)):
                if tmp > ans:
                    ans = tmp
    return ans


def is_palindrome(n):
    nstr = str(n)
    for i in range(0, len(nstr)//2):
        if nstr[i] != nstr[(i + 1)*-1]:
                return False
    return True


if __name__ == "__main__":
    print (str(compute()))
