#
# 0002 - Even Fibonacci numbers
#
# https://projecteuler.net/problem=2
# https://github.com/williamgrh/ProjectEulerSolutions
#

def compute():
    ans, a, b = 0, 1, 2
    while a <= 4000000:
        if a % 2 == 0:
            ans += a
        a, b = b, a + b
    return ans
        
if __name__ == "__main__":
    print ( str( compute() ) )