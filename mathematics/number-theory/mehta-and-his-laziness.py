# Mathematics > Number Theory > Mehta and his Laziness
# How will Mehta do these calculations?
#
# https://www.hackerrank.com/challenges/mehta-and-his-laziness/problem
# https://www.hackerrank.com/contests/infinitum-sep14/challenges/mehta-and-his-laziness
#

# le testcase 1 est en timeout avec Python3, ok avec pypy3
# j'ai dû rater une optimisation :-/

from fractions import Fraction

MAX = 1000000
even_squares = [False] * (MAX + 1)

for i in range(2, MAX, 2):
    x = i * i
    if x > MAX: break
    even_squares[x] = True


def diviseurs(n):
    div = [1]
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            div.append(i)
            if i != q:
                div.append(q)
        i += 1
    if n != 1:
        div.append(n)
    return div


def even_squares_divisors(n):
    nb = 1      # 1 est diviseur
    even = 0
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            nb += 1
            if even_squares[i]:
                even += 1
            if i != q:
                nb += 1
                if even_squares[q]:
                    even += 1
        i += 1

    return Fraction(even, nb)


for _ in range(int(input())):
    n = int(input())
    # d = diviseurs(n)
    # x = sum(1 for i in d if even_squares[i])
    # print(n, d, x, Fraction(x, len(d)))
    # print(Fraction(x, len(d)))
    print(even_squares_divisors(n))
