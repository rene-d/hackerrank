# Mathematics > Number Theory > Divisibility of Power
# Divisibility Test.
#
# https://www.hackerrank.com/challenges/divisibility-of-power/problem
# https://www.hackerrank.com/contests/infinitum-aug14/challenges/divisibility-of-power
# challenge id: 2597
#

import math

# if x = ∏ pi^ei, find(i,j) | x <=> Ai^(...) | x <=> Ai^(...) = ∏ pi^(ei+...)
# the worst case is x=2^54, Ai^(...) should equal to 2^(54+...) * ∏  pi^(...)
# 2^53 < 10^16 < 2^54, 2^16 is the upper limit for x

max_exp = math.ceil(math.log(10 ** 16) / math.log(2))   # 54


# modified but sufficient version of function find()
def find(i, j, n):
    if n == 0:              # stop the recursion
        return 0            # starting value 4 should be enough since 2^2^2 < 54 < 2^2^2^2

    if i > j or A[i] == 1 or A[i + 1] == 0:
        return 1            # normal case, 1^n = 1, n^0 = 1

    if A[i] == 0:
        return 0            # 0^n = 0

    if A[i] >= max_exp:
        return max_exp      # whatever A[i+1], if A[i]>=54 it's sufficient

    # the "real" function, value up to 54
    return min(max_exp, A[i] ** find(i + 1, j, n - 1))


n = int(input())
A = list(map(int, input().strip().split()))
A.append(0)     # for testing A[i+1] without IndexError

for _ in range(int(input())):
    i, j, x = map(int, input().strip().split())

    i -= 1      # A[] is 0 based
    j -= 1

    if x == 1 or i > j:
        a = 1           # trivial case
    else:
        a = pow(A[i], find(i + 1, j, 4), x)

    print('Yes' if a % x == 0 else 'No')
