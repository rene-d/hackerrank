# Mathematics > Algebra > Little Gaurav and Sequence
# Help Gaurav in calculating last digit of a sequence.
#
# https://www.hackerrank.com/challenges/little-gaurav-and-sequence/problem
#


def S_brutforce(n):
    s = 0
    i = 0
    while 2 ** i <= n:
        for j in range(0, n + 1):
            s += 2 ** (2 ** i + 2 * j)
        i += 1
    return s


def S(n):

    # s1 = 0
    # i = 0
    # while 2 ** i <= n:
    #     s1 += 2 ** (2 ** i)
    #     i += 1
    i = n
    k = 0
    while i != 0:
        i //= 2
        k += 1
    if k == 1:
        s1 = 2
    else:
        s1 = [6, 2, 8, 4, 0][(k - 2) % 5]

    # s2 = (4 ** (n + 1) - 1) // (4 - 1)
    # s2 = 1 mod 10     si n pair
    # s2 = 5 mod 10     si n impair
    s2 = 1 if n % 2 == 0 else 5

    return (s1 * s2) % 10


def test():
    for n in range(1, 100):
        s = S(n)
        assert (s % 10) == (S_brutforce(n) % 10)
        print("{:4} {}".format(n, s % 10))


for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print(0)
    else:
        s = S(n)
        print(s)
