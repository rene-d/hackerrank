# Algorithms > Dynamic Programming > Fibonacci Modified
# Compute the nth term of a Fibonacci sequence.
#
# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# https://www.hackerrank.com/contests/back2school14/challenges/fibonacci-modified
#

t1, t2, n = map(int, input().split())

for i in range(3, n + 1):
    t2, t1 = t1 + t2 ** 2, t2

print(t2)
