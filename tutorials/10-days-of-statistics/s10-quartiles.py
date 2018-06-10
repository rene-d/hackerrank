# Tutorials > 10 Days of Statistics > Day 1: Quartiles
# Calculate quartiles for an array of integers
#
# https://www.hackerrank.com/challenges/s10-quartiles/problem
# challenge id: 21248
#

def median(x):
    n = len(x)
    if n % 2 == 1:
        return x[n // 2]
    else:
        return (x[n // 2 - 1] + x[n // 2]) // 2


n = int(input())
x = list(map(int, input().split()))

x = sorted(x)

Q2 = median(x)
if n % 2 == 1:
    Q1 = median(x[0:(n // 2)])
    Q3 = median(x[(n // 2) + 1:])
else:
    Q1 = median(x[0:(n // 2)])
    Q3 = median(x[(n // 2):])

print(Q1)
print(Q2)
print(Q3)
