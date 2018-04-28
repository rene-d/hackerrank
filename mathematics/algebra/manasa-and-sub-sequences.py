# Mathematics > Algebra > Manasa and Sub-sequences
# Help Manasa in getting candies
#
# https://www.hackerrank.com/challenges/manasa-and-sub-sequences/problem
#

def manasa_simpliste(n):
    d = []
    for i in n:
        d.append(int(i))

    result = 0
    for i in range(1, 2 ** len(d)):
        x = 0
        j = i
        k = 0
        while j != 0:
            j, r = divmod(j, 2)
            if r == 1:
                x = x * 10 + d[k]
            k += 1
        result += x
    return result


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


def manasa(n):
    MOD = 1000000007
    result = 0

    m = len(n) - 1
    q = 1
    for c in n[::-1]:
        c = int(c)

        p = powmod(2, m, MOD)

        x = (c * p) % MOD
        result = (result + x * q) % MOD

        m -= 1
        q = (q * 11) % MOD

    return result % MOD


assert manasa("111") == 147
assert manasa("123") == 177

print(manasa(input()))
