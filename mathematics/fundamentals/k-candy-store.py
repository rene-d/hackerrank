# Mathematics > Fundamentals > K Candy Store
# In how many ways can you select K candies out of N different types of candies when each of the N candies are infinite in number?
#
# https://www.hackerrank.com/challenges/k-candy-store/problem
#

from math import factorial

def C(n, k):
    return factorial(n) // factorial(n - k) // factorial(k)

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    print(C(n + k - 1, n - 1) % 10 ** 9)
