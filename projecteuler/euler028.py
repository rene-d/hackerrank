"""
Project Euler #28: Number spiral diagonals

https://www.hackerrank.com/contests/projecteuler/challenges/euler028/
"""


# http://oeis.org/A114254
def A114254(n):
    return 1 + 10 * n ** 2 + (16 * n ** 3 + 26 * n) // 3


nb = int(input())
for i in range(nb):
    n = int(input()) // 2
    print(A114254(n) % 1000000007)
