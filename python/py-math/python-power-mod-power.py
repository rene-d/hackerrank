# Python > Math > Power - Mod Power
# Perform modular exponentiation in Python.
#
# https://www.hackerrank.com/challenges/python-power-mod-power/problem
#

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


a = int(input())
b = int(input())
m = int(input())

print(a ** b)
print(powmod(a, b, m))
