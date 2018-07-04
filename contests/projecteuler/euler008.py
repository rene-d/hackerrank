# ProjectEuler+ > Project Euler #8: Largest product in a series
# Playing with really really long numbers.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
# challenge id: 2634
#

for _ in range(int(input())):
    n, k = map(int, input().split())
    num = list(map(int, input()))

    m = 0

    for i in range(n - k):
        p = 1
        for j in range(i, i + k):
            p *= num[j]
        if p > m:
            m = p

    print(m)
