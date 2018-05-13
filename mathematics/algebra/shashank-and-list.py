# Mathematics > Algebra > Shashank and List
# Help Shashank in Huge calculations.
#
# https://www.hackerrank.com/challenges/shashank-and-list/problem
# https://www.hackerrank.com/contests/infinitum-may14/challenges/shashank-and-list
#

MOD = 1000000007


def powmod(x, k, MOD):
    """ fast exponentiation x^k % MOD """
    p = 1
    if k == 0:
        return p
    if k == 1:
        return x
    while k != 0:
        if k % 2 == 1:
            p = (p * x) % MOD
        x = (x * x) % MOD
        k //= 2
    return p


n = int(input())
answer = 1
for i in map(int, input().split()):
    answer *= powmod(2, i, MOD) + 1
    answer %= MOD
print(answer - 1)