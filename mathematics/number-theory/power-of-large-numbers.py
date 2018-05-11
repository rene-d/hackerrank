# Mathematics > Number Theory > Power of large numbers
# How much does Hackerland coach pay to get Cristiano Ronaldo to play for his team?
#
# https://www.hackerrank.com/challenges/power-of-large-numbers/problem
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


MOD = 1000000007

for _ in range(int(input())):
    sx, sy = input().split()

    # x = x modulo MOD
    x = 0
    for d in sx:
        x = (x * 10 + int(d)) % MOD

    # y = y modulo (MOD - 1)
    y = 0
    for d in sy:
        y = (y * 10 + int(d)) % (MOD - 1)

    # petit théorème de Fermat: https://fr.wikipedia.org/wiki/Petit_théorème_de_Fermat
    # p premier, m = n (mod p - 1)
    # alors a^m = a^n (mod p)

    # application ici: en calculant x^(y mod (p-1)) on a une valeur exacte modulo p

    print(powmod(x, y, MOD))
