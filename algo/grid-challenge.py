# Grid Challenge
# Find if it is possible to rearrange a square grid such that every
# row and every column is lexicographically sorted.
#
# https://www.hackerrank.com/challenges/grid-challenge/problem
#

def gridChallenge(n, grid):
    for i in range(n):
        for j in range(n - 1):
            if grid[j][i] > grid[j + 1][i]:
                return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
           grid.append(sorted(input()))
        result = gridChallenge(n, grid)
        print(result)
