# Tutorials > 10 Days of Statistics > Day 1: Interquartile Range
# Calculate the interquartile range.
#
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem
# challenge id: 21249
#

def median(x):
    n = len(x)
    if n % 2 == 1:
        return x[n // 2]
    else:
        return (x[n // 2 - 1] + x[n // 2]) / 2


n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

S = []
for x, f in zip(X, F):
    S.extend([x] * f)
S = sorted(S)

n = len(S)
if n % 2 == 1:
    Q1 = median(S[:(n // 2)])
    Q3 = median(S[(n // 2) + 1:])
else:
    Q1 = median(S[:(n // 2)])
    Q3 = median(S[(n // 2):])

print("{:.1f}".format(Q3 - Q1))
