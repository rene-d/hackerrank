# ProjectEuler+ > Project Euler #11: Largest product in a grid
# Getting started with matrices.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler011
# challenge id: 2637
#


grid = []
for _ in range(20):
	row = list(map(int, input().split()))
	grid.append(row)


pmax = 0

for i in range(20):
    for j in range(17):
        p = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        if p > pmax:
            pmax = p

for i in range(17):
    for j in range(20):
        p = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        if p > pmax:
            pmax = p

for i in range(17):
    for j in range(17):
        p = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        if p > pmax:
            pmax = p

for i in range(3, 20):
    for j in range(17):
        p = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
        if p > pmax:
            pmax = p

print(pmax)
