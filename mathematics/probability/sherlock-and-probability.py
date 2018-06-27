# Mathematics > Probability > Sherlock and Probability
# Help Sherlock in finding the probability.
#
# https://www.hackerrank.com/challenges/sherlock-and-probability/problem
# https://www.hackerrank.com/contests/infinitum-jul14/challenges/sherlock-and-probability
# challenge id: 2534
#

from fractions import Fraction


for _ in range(int(input())):
    n, k = map(int, input().split())
    bits = input()

    counter = [0] * (n + 1)
    for i, bit in enumerate(bits):
        counter[i + 1] = counter[i] + int(bit)

    p = 0
    for i, bit in enumerate(bits):
        if bit == "1":
            p += counter[min(n, i + k + 1)] - counter[max(0, i - k)]

    r = Fraction(p, n * n)
    print("{}/{}".format(r.numerator, r.denominator))
