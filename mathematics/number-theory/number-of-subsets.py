# Mathematics > Number Theory > Number of zero-xor subsets
# How many subsets with zero xor are here?
#
# https://www.hackerrank.com/challenges/number-of-subsets/problem
# https://www.hackerrank.com/contests/infinitum10/challenges/number-of-subsets
# challenge id: 4731
#

MOD = 1000000007

# la réponse est 2^(2^n - n)

for _ in range(int(input())):
    n = int(input())

    # généralisation du petit théorème de Fermat
    e = (pow(2, n, MOD - 1) - n) % (MOD - 1)

    r = pow(2, e, MOD)

    print(r)
