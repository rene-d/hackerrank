# Mathematics > Number Theory > Megaprime Numbers
# Count the number of primes in a given range that consist only of prime digits.
#
# https://www.hackerrank.com/challenges/megaprime-numbers/problem
# https://www.hackerrank.com/contests/w29/challenges/megaprime-numbers
# challenge id: 33596
#

from random import randrange
import sys


def miller_rabin(n, k=10):
    if n == 2 or n == 3 or n == 5 or n == 7: return True
    if n % 2 == 0 or n % 5 == 0: return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True


def to4(q):
    digits = [2, 3, 5, 7]
    q += 1
    e = 1
    n = 0
    while q != 0:
        q, r = divmod(q - 1, 4)
        n += e * digits[r]
        e *= 10
    return n


def from4(s):
    digits = [0, 0, 0, 1, 0, 2, 0, 3, 0, 0]
    n = -1
    for d in str(s):
        d = digits[int(d)]
        n = 4 * (n + 1) + d
    return n


start, end = map(int, input().split())

# find the number below start in 'base-2357'
carry = False
start4 = -1
for d in str(start):
    if carry:
        d = 3
    else:
        d = int(d)
        if d >= 7: d = 3
        elif d >= 5: d = 2
        elif d >= 3: d = 1
        elif d == 2: d = 0
        else:
            d = 3
            carry = True
            start4 -= 1
    start4 = 4 * (start4 + 1) + d
if start4 == -1:
    start4 = 0

# then iterate through numbers between start to end
answer = 0
i = start4
while True:
    n = to4(i)
    i += 1

    if n > end:
        break

    if n < start:
        continue

    if miller_rabin(n):
        answer += 1

print(answer)
