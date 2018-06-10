# Tutorials > 10 Days of Statistics > Day 0: Mean, Median, and Mode
# Compute the mean, median, mode, and standard deviation.
#
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# challenge id: 21180
#

from itertools import groupby

n = int(input())
x = list(map(int, input().split()))

# la moyenne arithmétique
m = sum(x) / len(x)
print("{:.1f}".format(m))

# la valeur médiane
x = sorted(x)
if n % 2 == 1:
    m = x[n // 2]
    print(m)
else:
    m = (x[n // 2 - 1] + x[n // 2]) / 2
    print("{:.1f}".format(m))

# la classe modale
# on trie les paires par longueur décroissante: la première sera la plus grande en valeur absolue
m = sorted([-len(list(g)), int(k)] for k, g in groupby(x))
print(m[0][1])
