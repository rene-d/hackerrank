# Tutorials > 10 Days of Statistics > Day 0: Weighted Mean
# Compute the weighted mean.
#
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# challenge id: 21217
#

n = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

m = sum(x * w for x, w in zip(X, W)) / sum(W)
print("{:.1f}".format(m))
