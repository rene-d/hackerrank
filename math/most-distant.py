# Most Distant
# Measure the gap between the two most distant coordinates.
#
# https://www.hackerrank.com/challenges/most-distant/problem
#

# la plus grande distance se situe forcément entre deux extrêmités
# du quadrilatère entourant les points

n = int(input())
x, y = map(int, input().split())

x0, y0, x1, y1 = x, y, x, y

for _ in range(1, n):
    x, y = map(int, input().split())
    x0 = min(x0, x)
    x1 = max(x1, x)
    y0 = min(y0, y)
    y1 = max(y1, y)

print(max(x1 - x0,
          y1 - y0,
          (x0 ** 2 + y1 ** 2) ** 0.5,
          (x0 ** 2 + y0 ** 2) ** 0.5,
          (x1 ** 2 + y1 ** 2) ** 0.5,
          (x1 ** 2 + y0 ** 2) ** 0.5))
