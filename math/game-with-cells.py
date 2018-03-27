# Army Game
# Find the minimum number of supply packages Luke must drop to supply all of his army bases.
#
# https://www.hackerrank.com/challenges/game-with-cells/problem
#


n, m = map(int, input().split())
r = ((n + 1) // 2) * ((m + 1) // 2)
print(r)
