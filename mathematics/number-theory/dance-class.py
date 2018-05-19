# Mathematics > Number Theory > Dancing in Pairs
# Find out if they can dance in pairs?
#
# https://www.hackerrank.com/challenges/dance-class/problem
# https://www.hackerrank.com/contests/infinitum-jun14/challenges/dance-class
# challenge id: 2561
#

from decimal import Decimal

for _ in range(int(input())):
    n = Decimal(input())
    p = n.sqrt()
    print(["even", "odd"][int(p) % 2])
