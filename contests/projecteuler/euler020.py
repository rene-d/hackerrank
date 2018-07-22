# ProjectEuler+ > Project Euler #20: Factorial digit sum
# When complexities go from one extreme to the other.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler020
# challenge id: 2646
#

from math import factorial

for _ in range(int(input())):
    n = int(input())

    print(sum(int(d) for d in str(factorial(n))))
