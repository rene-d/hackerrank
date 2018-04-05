# Sherlock and The Beast
# Find the largest number following some rules having N digits.
#
# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
#


t = int(input())
for _ in range(t):
    n = int(input())

    # The number of 3's it contains is divisible by 5.
    # The number of 5's it contains is divisible by 3.

    # on essaie avec n chiffres 5 et on diminue
    # tant que la propriété (3) n'est pas vérifiée
    m = n
    while m % 3 != 0:
        m -= 5

    if m < 0:
        print("-1")
    else:
        print("5" * m + "3" * (n - m))
