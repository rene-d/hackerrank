# Mathematics > Algebra > Sherlock and Square
# Help Sherlock in finding the total side lengths of squares.
#
# https://www.hackerrank.com/challenges/sherlock-and-square/problem
# https://www.hackerrank.com/contests/w11/challenges/sherlock-and-square
# challenge id: 4429
#

MOD = 1000000007

for _ in range(int(input())):
    n = int(input())
    print((pow(2, n + 1, MOD) + 2) % MOD)
